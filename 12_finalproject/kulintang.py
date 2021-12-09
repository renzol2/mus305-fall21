import musx
import pythonosc.udp_client
import scosc  # in this script's directory
from phrases import Note
from transcriptions.duyug_cr_1 import DUYUG_CR_1_OPENING, DUYUG_CR_1_BODY
from transcriptions.duyug_cr_12 import DUYUG_CR_12_BODY, DUYUG_CR_12_CLOSING

OSC_ADDRESS = '/musx/kulintang'


def compose_kulintang(score: musx.Score, notes: list[Note], dur: float, amps: tuple[float, float], tempo: int):
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
                    OSC_ADDRESS, score.now + now, gong_num, 0, dur, amp)
                score.add(msg)
        else:
            # In this case, we play 2 notes (gong_num is a 2-tuple)
            msgs = [
                scosc.OscMessage(
                    OSC_ADDRESS, score.now + now, num, 0, dur, amp
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
    amps = 0.5, 1.2
    tempo = 100

    markov_kulintang_body = generate_pattern(DUYUG_CR_1_BODY + DUYUG_CR_12_BODY, order=10, length=1000)
    markov_kulintang_piece = DUYUG_CR_1_OPENING + \
        markov_kulintang_body + DUYUG_CR_12_CLOSING
    # pretty_print_kulintang_piece(markov_kulintang_piece)

    seq = musx.Seq()
    score = musx.Score(out=seq)
    score.compose(compose_kulintang(
        score, markov_kulintang_piece, dur, amps, tempo))
    scosc.oscplayer(seq, oscout)
