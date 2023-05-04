import musx
import math
import pythonosc.udp_client
import scosc  # in this script's directory
from phrases import (
    Note,
    DUYUG_DABAKAN_SAMPLE_PATTERN,
    BINALIG_DABAKAN_SAMPLE_PATTERN,
    BINALIG_BABANDIR_SAMPLE_PATTERN,
    DUYUG_BABANDIR_SAMPLE_PATTERN_1,
    SCALE,
)
from transcriptions.duyug_cr_1 import (
    DUYUG_CR_1_OPENING,
    DUYUG_CR_1_BODY,
    DUYUG_CR_1,
    DUYUG_CR_1_CLOSING,
)
from transcriptions.duyug_cr_12 import (
    DUYUG_CR_12_BODY,
    DUYUG_CR_12_CLOSING,
    DUYUG_CR_12,
)
from transcriptions.duyug_cr_13 import DUYUG_CR_13, DUYUG_CR_13_BODY
from transcriptions.binalig_cr_23 import (
    BINALIG_CR_23,
    BINALIG_CR_23_OPENING,
    BINALIG_CR_23_BODY,
    BINALIG_CR_23_CLOSING,
)
from tuning import (
    UNIVERSITY_PHILIPPINES_TUNING,
    BUTOCAN_TUNING,
    ANDRE_TUNING,
    JAVANESE_TUNING,
)

KULINTANG_OSC_ADDRESS = "/musx/kulintang"
DABAKAN_OSC_ADDRESS = "/musx/dabakan"
BABANDIR_OSC_ADDRESS = "/musx/babandir"
KULINTANG_TUNED_OSC_ADDRESS = "/musx/kulintangTuned"


def get_composition_length(notes: list[Note]) -> float:
    """
    Get the total number of beats in the composition
    """
    total_length = 0
    for _, beat_length, _ in notes:
        total_length += beat_length
    return total_length


def compose_kulintang(
    score: musx.Score,
    notes: list[Note],
    dur: float,
    amps: tuple[float, float],
    tempo: int,
    address: str = KULINTANG_OSC_ADDRESS,
    tuning: list[int] = None,
):
    """
    Adds kulintang notes to the given score
    """
    non_accent_amp, accent_amp = amps
    for gong_num, beat_length, accent in notes:
        now = 0
        amp = accent_amp if accent else non_accent_amp

        # Add notes to score, depending on if there are 1-2 notes at the same time
        if isinstance(gong_num, int):
            # Avoid adding notes if there's a rest
            if gong_num != 0:
                # If using alternate tuning, tune gongs by 12-TET half-step, rather than gong number
                if address == KULINTANG_TUNED_OSC_ADDRESS:
                    gong_num = tuning[gong_num - 1]
                # If not a kulintang, randomize between percussive hits
                elif address != KULINTANG_OSC_ADDRESS:
                    gong_num = musx.between(0, 4)
                # Add message to score
                msg = scosc.OscMessage(address, score.now + now, gong_num, 0, dur, amp)
                score.add(msg)
        else:
            # In this case, we play 2 notes (gong_num is a tuple)
            msgs = [
                scosc.OscMessage(
                    address,
                    score.now + now,
                    tuning[num - 1] if address == KULINTANG_TUNED_OSC_ADDRESS else num,
                    0,
                    dur,
                    amp,
                )
                for num in gong_num
            ]
            for msg in msgs:
                score.add(msg)

        now += musx.intempo(beat_length, tempo)
        yield now


def generate_pattern(
    original_pattern: list, order: int = musx.between(1, 4), length: int = None
):
    rules = musx.markov_analyze(original_pattern, order)
    gen = musx.markov(rules)
    return [
        next(gen) for _ in range(len(original_pattern) if length is None else length)
    ]


def pretty_print_kulintang_piece(notes: list[Note]):
    for note in notes:
        print(note)


if __name__ == "__main__":
    oscout = pythonosc.udp_client.SimpleUDPClient("127.0.0.1", 57120)
    print(oscout)

    # Basic parameters
    dur = 0.5
    amps = 0.5, 0.9  # non-accent, accent
    tempo = 70
    use_alternate_tuning = False
    alternate_tuning = UNIVERSITY_PHILIPPINES_TUNING
    # print(alternate_tuning)

    # Compositional parameters
    use_markov = True
    kulintang_part = SCALE # overwritten if use_markov=True

    # Markov chain parameters
    # markov_data = SCALE
    markov_data = BINALIG_CR_23_BODY
    # markov_data = (
    #     DUYUG_CR_1_BODY + DUYUG_CR_12_BODY + DUYUG_CR_13_BODY
    # )
    markov_order = 12  # duyug: ~3-10, binalig: ~12
    # opening_pattern = DUYUG_CR_1_OPENING
    # closing_pattern = DUYUG_CR_12_CLOSING
    opening_pattern = BINALIG_CR_23_OPENING
    closing_pattern = BINALIG_CR_23_CLOSING
    num_notes = 2700

    # Other instrument parameters
    play_dabakan = False 
    play_babandir = False 
    dabakan_pattern = DUYUG_DABAKAN_SAMPLE_PATTERN
    babandir_pattern = DUYUG_BABANDIR_SAMPLE_PATTERN_1

    if use_markov:
        # Construct piece through Markov chains
        markov_kulintang_body = generate_pattern(
            markov_data, order=markov_order, length=num_notes
        )
        kulintang_part = opening_pattern + markov_kulintang_body + closing_pattern
    pretty_print_kulintang_piece(kulintang_part)

    # Get dabakan score
    total_beats = get_composition_length(kulintang_part)
    dabakan_pattern_length = get_composition_length(dabakan_pattern)
    num_dabakan_reps = math.floor(total_beats / dabakan_pattern_length)
    dabakan_part = dabakan_pattern * num_dabakan_reps

    # Get babandir score
    babandir_pattern_length = get_composition_length(babandir_pattern)
    num_babandir_reps = math.floor(total_beats / babandir_pattern_length)
    babandir_part = babandir_pattern * num_babandir_reps

    # Setup score
    seq = musx.Seq()
    score = musx.Score(out=seq)

    # Compose score with parameters
    kulintang_address = (
        KULINTANG_TUNED_OSC_ADDRESS if use_alternate_tuning else KULINTANG_OSC_ADDRESS
    )
    tuning = alternate_tuning if use_alternate_tuning else None
    composers = [
        compose_kulintang(
            score, kulintang_part, dur, amps, tempo, kulintang_address, tuning
        )
    ]
    if play_babandir:
        composers.append(
            compose_kulintang(
                score, babandir_part, dur, amps, tempo, BABANDIR_OSC_ADDRESS
            )
        )
    if play_dabakan:
        composers.append(
            compose_kulintang(
                score, dabakan_part, dur, amps, tempo, DABAKAN_OSC_ADDRESS
            )
        )
    score.compose(composers)

    # Write to file
    # track0 = musx.MidiFile.metatrack()
    # file = musx.MidiFile('kulintang.mid', [track0, score.out]).write()

    # Send to SuperCollider
    scosc.oscplayer(seq, oscout)
