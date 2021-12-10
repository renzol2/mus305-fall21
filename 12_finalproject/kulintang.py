import musx
import math
import pythonosc.udp_client
import scosc  # in this script's directory
from phrases import Note, DUYUG_DABAKAN_SAMPLE_PATTERN, BINALIG_DABAKAN_SAMPLE_PATTERN
from transcriptions.duyug_cr_1 import DUYUG_CR_1_OPENING, DUYUG_CR_1_BODY
from transcriptions.duyug_cr_12 import DUYUG_CR_12_BODY, DUYUG_CR_12_CLOSING, DUYUG_CR_12
from transcriptions.duyug_cr_13 import DUYUG_CR_13, DUYUG_CR_13_BODY
from transcriptions.binalig_cr_23 import BINALIG_CR_23, BINALIG_CR_23_OPENING, BINALIG_CR_23_BODY, BINALIG_CR_23_CLOSING

KULINTANG_OSC_ADDRESS = '/musx/kulintang'
DABAKAN_OSC_ADDRESS = '/musx/dabakan'


def get_composition_length(notes: list[Note]) -> float:
    '''
    Get the total number of beats in the composition
    '''
    total_length = 0
    for _, beat_length, _ in notes:
        total_length += beat_length
    return total_length


def compose_kulintang(score: musx.Score, notes: list[Note], dur: float, amps: tuple[float, float], tempo: int, address: str = KULINTANG_OSC_ADDRESS):
    '''
    Adds a single kulintang notes to the given score
    '''
    non_accent_amp, accent_amp = amps
    for gong_num, beat_length, accent in notes:
        now = 0
        amp = accent_amp if accent else non_accent_amp

        # Add notes to score, depending on if there are 1-2 notes at the same time
        if isinstance(gong_num, int):
            # Avoid adding notes if there's a rest
            if gong_num != 0:
                msg = scosc.OscMessage(
                    address, score.now + now, gong_num, 0, dur, amp)
                score.add(msg)
        else:
            # In this case, we play 2 notes (gong_num is a 2-tuple)
            msgs = [
                scosc.OscMessage(
                    address, score.now + now, num, 0, dur, amp
                ) for num in gong_num
            ]
            for msg in msgs:
                score.add(msg)

        now += musx.intempo(beat_length, tempo)
        yield now


def generate_pattern(original_pattern: list, order: int = musx.between(1, 4), length: int = None):
    rules = musx.markov_analyze(original_pattern, order)
    gen = musx.markov(rules)
    return [next(gen) for _ in range(len(original_pattern) if length is None else length)]


def pretty_print_kulintang_piece(notes: list[Note]):
    for note in notes:
        print(note)


if __name__ == '__main__':
    oscout = pythonosc.udp_client.SimpleUDPClient('127.0.0.1', 57120)
    print(oscout)

    dur = 0.5
    amps = 0.5, 0.9
    tempo = 69
    markov_order = 12  # duyug: ~3-10, binalig: ~12
    num_notes = 200

    markov_kulintang_body = generate_pattern(
        BINALIG_CR_23_BODY, order=markov_order, length=num_notes)
    markov_kulintang_piece = BINALIG_CR_23_OPENING + \
        markov_kulintang_body + BINALIG_CR_23_CLOSING
    # pretty_print_kulintang_piece(markov_kulintang_piece)

    # Get dabakan score
    dabakan_pattern = BINALIG_DABAKAN_SAMPLE_PATTERN
    total_beats = get_composition_length(markov_kulintang_piece)
    dabakan_pattern_length = get_composition_length(
        dabakan_pattern)
    num_dabakan_reps = math.floor(total_beats / dabakan_pattern_length)

    # Setup score
    seq = musx.Seq()
    score = musx.Score(out=seq)

    # Compose score with parameters
    score.compose([
        compose_kulintang(score, markov_kulintang_piece, dur,
                          amps, tempo, KULINTANG_OSC_ADDRESS),
        compose_kulintang(score, dabakan_pattern *
                          num_dabakan_reps, dur, amps, tempo, DABAKAN_OSC_ADDRESS),
    ])

    # Write to file
    # track0 = musx.MidiFile.metatrack()
    # file = musx.MidiFile('kulintang.mid', [track0, score.out]).write()

    # Send to SuperCollider
    scosc.oscplayer(seq, oscout)
