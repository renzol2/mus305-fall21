import math
from random import randint, random, randrange, shuffle
from musx import Score, Seq, MidiFile, Note
from musx.interval import Interval
from musx.midi.gm import AcousticGrandPiano, Banjo, Cabasa, Claves, HandClap, Kalimba, Marimba, Vibraphone, Xylophone
from musx.pitch import Pitch, scale
from musx.tools import rand


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


def get_claps_composer(score: Score, root_keynum: int, repeats: int, rhy: float, dur: float, lower_instr_chan: int, num_notes: int = 8):
    claps = [x for x in clapper(
        get_shuffled_maj_pent(root_keynum, num_notes), repeats, True)]
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

    high = [Pitch('d#2'), Pitch('c#4'), Pitch('f#5')][randint(0, 2)]
    mid = Interval('-P8').transpose(high)
    low = Interval('-P8').transpose(mid)
    rhy = 0.1 + (random() * 0.3)
    dur = 0.1
    num_notes = randint(3, 16)
    num_repeats = 4
    print(high, rhy, dur, num_notes)
    score.compose([
        [0, get_claps_composer(score, high.keynum(), num_repeats, rhy, dur, 1, num_notes)],
        [0, get_claps_composer(score, mid.keynum(), math.floor(num_repeats / 2), rhy * 2, dur * 2, 3, num_notes)],
        [0, get_claps_composer(score, low.keynum(), math.floor(num_repeats / 4), rhy * 4, dur * 4, 3, num_notes)],
    ])

    filename = 'claps.mid'
    MidiFile(filename, [meta, seq]).write()
    print(f'Wrote {filename}')
