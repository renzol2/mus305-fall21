from musx import Interval, Pitch, Score, Seq, MidiFile, Note
from musx.midi.gm import Kalimba
import random

maj_intervals = [Interval('M3'), Interval('P5')]
min_intervals = [Interval('m3'), Interval('P5')]
dim_intervals = [Interval('m3'), Interval('d5')]
aug_intervals = [Interval('M3'), Interval('+5')]

possible_intervals = [
    maj_intervals,
    min_intervals,
    dim_intervals,
    aug_intervals,
]


def create_rand_chord(low: int, high: int) -> list[int]:
    # Highest possible root keynum
    high_bound = high - Interval('m6').semitones()
    rand_keynum = random.randint(low, high_bound)
    rand_pitch = Pitch.from_keynum(rand_keynum)
    chord = [rand_keynum] + [i.transpose(rand_pitch).keynum(
    ) for i in possible_intervals[random.randint(0, len(possible_intervals) - 1)]]
    return chord


def ranchords(num: int, low: int, high: int):
    """
    Define a generator ranchords(num, low, high) that returns a 
    specified number of randomly selected major, minor, diminished, 
    or augmented triads whose lowest and highest notes (keynums) lie 
    within the lower and upper bounds (inclusive) specified to the function. 
    Each chord is represented as list of three key numbers sorted low to high.
    """
    count = 0
    while count < num:
        yield create_rand_chord(low, high)
        count += 1


def play_chords(score: Score, chords: list[list[int]], rhy: float, dur: float, amp: float):
    for chord in chords:
        for keynum in chord:
            note = Note(time=score.now, duration=dur,
                        pitch=keynum, amplitude=amp, instrument=1)
            score.add(note)
        yield rhy


if __name__ == '__main__':
    chords = [c for c in ranchords(22, 60, 80)]
    print(chords)

    # make a midi file that uses your ranchords()
    seq = Seq()
    meta = MidiFile.metatrack(ins={ 1: Kalimba })
    score = Score(out=seq)

    composer = play_chords(score, chords, rhy=0.5, dur=0.45, amp=1)
    score.compose([composer])
    filename = 'ranchords.mid'
    MidiFile(filename, [meta, seq]).write()
    print(f'Wrote {filename}')
