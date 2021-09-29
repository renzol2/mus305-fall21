import musx
from musx.gens import cycle
from musx.midi.gm import AcousticBass, AcousticGrandPiano, AcousticSnare, BassDrum1, ClosedHiHat, ElectricSnare, OpenHiHat
from musx.midi.midifile import MidiFile
from musx.note import Note
from musx.rhythm import intempo
from musx.score import Score
from musx.seq import Seq

CLOSED_HI_HAT = ClosedHiHat + 1
OPEN_HI_HAT = OpenHiHat + 1
SNARE = ElectricSnare + 1
BASS_DRUM = BassDrum1 + 1
REST = 'r'


def dnb_hi_hat(score: Score, tempo: int, ampl: float):
    rhy = intempo(0.5, tempo)
    dur = intempo(0.5, tempo)
    acc_amp = 0.8
    non_acc_amp = 0.2

    # + + + + | + + + + | + + + + | + o + +
    hi_hat_bar = [CLOSED_HI_HAT] * 4
    hi_hat_pattern = hi_hat_bar*3 + \
        [CLOSED_HI_HAT] + [OPEN_HI_HAT] + [CLOSED_HI_HAT]*2

    print(hi_hat_pattern)
    pat = cycle(hi_hat_pattern)
    for i in range(len(hi_hat_pattern)):
        k = next(pat)

        # Accent every other note and open hi-hat
        amp = acc_amp if i % 2 == 0 or i == 13 else non_acc_amp

        m = Note(time=score.now, duration=dur, pitch=k,
                 amplitude=ampl * amp, instrument=9)
        score.add(m)
        yield rhy


def dnb_drums(score: Score, tempo: int, ampl: float):
    rhy = intempo(0.5, tempo)
    dur = intempo(0.2, tempo)
    amp = 0.7

    kick_snare_pattern = [
        BASS_DRUM, REST, SNARE, REST, 
        REST, BASS_DRUM, SNARE, REST,
        REST, BASS_DRUM, SNARE, BASS_DRUM,
        REST, BASS_DRUM, SNARE, REST,
    ]
    pat = cycle(kick_snare_pattern)
    for _ in range(len(kick_snare_pattern)):
        k = next(pat)
        if k != REST:
            m = Note(time=score.now, duration=dur, pitch=k,
                     amplitude=ampl * amp, instrument=9)
            score.add(m)
        yield rhy


if __name__ == '__main__':
    tempo = 170
    track0 = MidiFile.metatrack(ins={0: AcousticGrandPiano, 1: AcousticBass})

    score = Score(out=Seq())

    play = []

    for x in range(0, 15, 2):
        play.extend([[x * 1.4, dnb_hi_hat(score, tempo, 1)],
                    [x * 1.4, dnb_drums(score, tempo, 1)]])

    score.compose(play)
    file = MidiFile("dnb_hihat.mid", [track0, score.out]).write()
