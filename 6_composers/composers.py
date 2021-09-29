import musx
from musx.gens import choose, cycle
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
BASS_OR_REST = 'bass or snare'
SNARE_OR_REST = 'snare or rest'
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
    amp = 0.95

    bass_or_rest = choose(items=[BASS_DRUM, REST], weights=[0.25, 0.75])
    
    # eighth notes
    # b=bass, s=snare, .=rest, ?=bass or rest
    # . . s . . . s . | . . s . . . s . 
    # b . . . . b . . | ? ? ? ? ? ? ? ?
    kick_snare_pattern = [
        BASS_DRUM, REST, SNARE, REST,
        REST, BASS_DRUM, SNARE, REST,
        BASS_OR_REST, BASS_OR_REST, SNARE, BASS_OR_REST,
        BASS_OR_REST, BASS_OR_REST, SNARE, BASS_OR_REST,
    ]
    pat = cycle(kick_snare_pattern)
    for _ in range(len(kick_snare_pattern)):
        k = next(pat)

        # Choose bass drum or rest if noted
        pitch = k
        if pitch == BASS_OR_REST:
            pitch = next(bass_or_rest)

        if pitch != REST:
            m = Note(time=score.now, duration=dur, pitch=pitch,
                     amplitude=ampl * amp, instrument=9)
            score.add(m)
        yield rhy


def dnb_ghost_notes(score: Score, tempo: int, ampl: float):
    rhy = intempo(0.25, tempo)
    dur = intempo(0.1, tempo)
    amps = cycle([.6, .5, .7, .5, 1, .6, .5, .7, .5, 0.8])

    snare_or_rest = choose(items=[SNARE, REST], weights=[0.25, 0.75])

    # 16th notes
    # g=ghost, .=rest, ?=ghost or rest
    # |: . . . . | . g . g | . g . g | . g . g :|
    rest_pat = [REST] * 4
    ghost_note_pat = [REST, SNARE_OR_REST,
                      REST, SNARE_OR_REST]
    ghost_note_bar_pat = rest_pat + ghost_note_pat*3
    ghost_note_bars_pat = ghost_note_bar_pat * 2
    pat = cycle(ghost_note_bars_pat)

    for _ in range(len(ghost_note_bars_pat)):
        k = next(pat)

        pitch = k
        if pitch == SNARE_OR_REST:
            pitch = next(snare_or_rest)

        if pitch != REST:
            a = next(amps)
            m = Note(time=score.now, duration=dur, pitch=pitch,
                     amplitude=ampl * a, instrument=9)
            score.add(m)
        yield rhy


if __name__ == '__main__':
    tempo = 180
    track0 = MidiFile.metatrack(ins={0: AcousticGrandPiano, 1: AcousticBass})

    score = Score(out=Seq())

    play = []

    time_constant = 1.3325
    for x in range(0, 15, 2):
        section_start = x * time_constant
        play.extend([[section_start, dnb_hi_hat(score, tempo, 1)],
                    [section_start, dnb_drums(score, tempo, 1)],
                    [section_start, dnb_ghost_notes(score, tempo, 1)]])

    score.compose(play)
    file = MidiFile("dnb_hihat.mid", [track0, score.out]).write()
