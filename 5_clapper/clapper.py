from random import shuffle
from musx import Score, Seq, MidiFile, Note
from musx.interval import Interval
from musx.midi.gm import AcousticGrandPiano, Banjo, Cabasa, Claves, HandClap, Kalimba, Marimba, Vibraphone, Xylophone
from musx.pitch import Pitch, scale


def clapper(trope, repeat: int, wraparound: bool = False):
    counterpoint_offset = 0
    rotation = 0
    while rotation != len(trope):
        for _ in range(repeat):
            for i in range(len(trope)):
                yield [trope[i], trope[(i + counterpoint_offset) % len(trope)]]
        counterpoint_offset += 1
        rotation += 1

    if wraparound:
        for _ in range(repeat):
            for i in range(len(trope)):
                yield [trope[i], trope[i]]


def play_claps(score: Score, claps: list[list[int]], rhy: float, dur: float, amp: float, lower_instr_chan: int = 1):
    for clap in claps:
        for i, note in enumerate(clap):
            note = Note(time=score.now, duration=dur, pitch=note,
                        amplitude=amp, instrument=lower_instr_chan + i + 1)
            score.add(note)
        yield rhy


def get_shuffled_maj_pent(root_keynum: int, num_notes: int = 16):
    notes = scale(root_keynum, num_notes, 2, 3, 2, 2, 3)
    shuffle(notes)
    return notes


def get_claps_composer(score: Score, root_keynum: int, repeats: int, rhy: float, dur: float, lower_instr_chan: int):
    claps = [x for x in clapper(
        get_shuffled_maj_pent(root_keynum, 8), repeats, True)]
    return play_claps(score, claps, rhy, dur, 1.0, lower_instr_chan)


if __name__ == '__main__':

    seq = Seq()
    CLAPPER_1, CLAPPER_2, CLAPPER_3, CLAPPER_4 = 1, 2, 3, 4
    meta = MidiFile.metatrack(
        ins={
            CLAPPER_1: Kalimba,
            CLAPPER_2: Marimba,
            CLAPPER_3: AcousticGrandPiano,
            CLAPPER_4: Vibraphone
        })
    score = Score(out=seq)

    high = Pitch('f#4')
    mid = Interval('-P8').transpose(high)
    low = Interval('-P8').transpose(mid)
    rhy = 0.2
    dur = 0.1
    score.compose([
        get_claps_composer(score, high.keynum(), 4, rhy, dur, 1),
        get_claps_composer(score, mid.keynum(), 2, rhy * 2, dur * 2, 3),
        get_claps_composer(score, low.keynum(), 1, rhy * 4, dur * 4, 3)
    ])

    filename = 'claps.mid'
    MidiFile(filename, [meta, seq]).write()
    print(f'Wrote {filename}')
