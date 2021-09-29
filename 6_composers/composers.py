import musx
from musx.gens import cycle
from musx.midi.gm import AcousticBass, AcousticGrandPiano, ClosedHiHat, OpenHiHat
from musx.midi.midifile import MidiFile
from musx.note import Note
from musx.rhythm import intempo
from musx.score import Score
from musx.seq import Seq


def dnb_hi_hat(score: Score, tempo: int, ampl: float):
    rhy = intempo(0.5, tempo)
    dur = intempo(0.5, tempo)
    acc_amp = 0.8
    non_acc_amp = 0.4

    # + + + + | + + + + | + + + + | + o + +
    hi_hat_pattern = [42]*5 + [46] + [42]*2

    pat = cycle(hi_hat_pattern)
    for i in range(8):
        x = next(pat)

        # Accent every other note and open hi-hat
        amp = acc_amp if i % 2 == 0 or i == 5 else non_acc_amp

        m = Note(time=score.now, duration=dur, pitch=x,
                 amplitude=ampl * amp, instrument=9)
        score.add(m)
        yield rhy


if __name__ == '__main__':
    tempo = 170
    track0 = MidiFile.metatrack(ins={0: AcousticGrandPiano, 1: AcousticBass})

    score = Score(out=Seq())

    play = [[t * 1.4, dnb_hi_hat(score, tempo, 1)] for t in range(0, 15)]

    score.compose(play)
    file = MidiFile("dnb_hihat.mid", [track0, score.out]).write()
