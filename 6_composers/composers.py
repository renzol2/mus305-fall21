import musx
from musx.gens import choose, cycle
from musx.interval import Interval
from musx.midi.gm import AcousticBass, AcousticGrandPiano, AcousticSnare, BassDrum1, ClosedHiHat, Cowbell, ElectricBass_finger, ElectricPiano1, ElectricPiano2, ElectricSnare, OpenHiHat, RideCymbal1, RideCymbal2, SideStick
from musx.midi.midifile import MidiFile
from musx.note import Note
from musx.pitch import Pitch
from musx.ran import between, odds, pick
from musx.rhythm import intempo
from musx.score import Score
from musx.seq import Seq

CLOSED_HI_HAT = ClosedHiHat + 1
OPEN_HI_HAT = OpenHiHat + 1
RIDE1 = RideCymbal1 + 1
RIDE2 = RideCymbal2 + 1
COWBELL = Cowbell + 1
SNARE = ElectricSnare + 1
ACOUSTIC_SNARE = AcousticSnare + 1
SIDE_STICK = SideStick + 1
BASS_DRUM = BassDrum1 + 1
BASS_OR_REST = 'bass or snare'
SNARE_OR_REST = 'snare or rest'
REST = 'r'


def dnb_hi_hat(score: Score, tempo: int, ampl: float, sound: int = CLOSED_HI_HAT):
    '''
    Generates hi-hats on eighth notes with alternating accents.
    Can substitute closed hi-hat for other sounds.
    '''
    rhy = intempo(0.5, tempo)
    dur = intempo(0.5, tempo)
    acc_amp = 0.8
    non_acc_amp = 0.2

    # >   >     >   >     >   >     > > >
    # + + + + | + + + + | + + + + | + o + +
    hi_hat_bar = [sound] * 4
    hi_hat_pattern = hi_hat_bar*3 + \
        [sound] + [OPEN_HI_HAT] + [sound]*2

    pat = cycle(hi_hat_pattern)
    for i in range(len(hi_hat_pattern)):
        k = next(pat)

        # Accent every other note and open hi-hat
        amp = acc_amp if i % 2 == 0 or i == 13 else non_acc_amp

        m = Note(time=score.now, duration=dur, pitch=k,
                 amplitude=ampl * amp, instrument=9)
        score.add(m)
        yield rhy


def dnb_drums(score: Score, tempo: int, ampl: float, snare_sound: int = SNARE):
    '''
    Generates random kick & snare patterns.
    '''
    rhy = intempo(0.5, tempo)
    dur = intempo(0.2, tempo)
    amp = 0.95

    bass_or_rest = choose(items=[BASS_DRUM, REST], weights=[0.25, 0.75])

    # eighth notes
    # b=bass, s=snare, .=rest, ?=bass or rest
    # . . s . . . s . | . . s . . . s .
    # b . . . . b . . | ? ? ? ? ? ? ? ?
    kick_snare_pattern = [
        BASS_DRUM, REST, snare_sound, REST,
        REST, BASS_DRUM, snare_sound, REST,
        BASS_OR_REST, BASS_OR_REST, snare_sound, BASS_OR_REST,
        BASS_OR_REST, BASS_OR_REST, snare_sound, BASS_OR_REST,
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
    '''
    Generates random ghost notes at 16th note subdivisions.
    '''
    rhy = intempo(0.25, tempo)
    dur = intempo(0.1, tempo)
    amps = cycle([.6, .5, .7, .5, 1, .6, .5, .7, .5, 0.8])

    snare_or_rest = choose(items=[SNARE, REST], weights=[0.25, 0.75])

    # 16th notes
    # g=ghost or rest .=rest
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


def create_rand_chord(low: int, high: int) -> list[int]:
    # Highest possible root keynum
    high_bound = high - Interval('P5').semitones()
    rand_keynum = between(low, high_bound)
    rand_pitch = Pitch.from_keynum(rand_keynum)

    # Combine root with notes transposed up m3 and P5
    chord = [rand_keynum] + [i.transpose(rand_pitch).keynum(
    ) for i in [Interval('m3'), Interval('P5'), Interval('m7')]]

    return chord


def dnb_chords(score: Score, tempo: int, low: int, high: int, num_chords: int = 3, amp: float = 0.6, chords: int = ElectricPiano1):
    '''
    Adds a variable number of electric piano and bass chords in measure
    '''

    # Generate random chords
    chords = [create_rand_chord(low, high) for _ in range(num_chords)]

    # Find start times for each
    num_subdivisions = 16
    all_times = [i for i in range(num_subdivisions)]
    chosen_times = []
    for _ in range(num_chords):
        rand_index = between(0, len(all_times))
        rand_time = all_times[rand_index]
        all_times = all_times[:rand_index] + all_times[rand_index+1:]
        chosen_times.append(rand_time)

    chosen_times.sort()
    chosen_times.append(16)

    for i, chord in enumerate(chords):
        time = (chosen_times[i+1] - chosen_times[i]) / 2
        rhy = intempo(time, tempo)
        dur = intempo(time, tempo)

        # Add bass
        bass = Note(time=score.now, duration=dur, pitch=chord[0] - 12,
                    amplitude=amp, instrument=1)
        score.add(bass)

        # Add electric piano
        for keynum in chord:
            m = Note(time=score.now, duration=dur, pitch=keynum,
                     amplitude=amp, instrument=0)
            score.add(m)
        yield rhy


def dnb_track(score: Score, measures: int, tempo: int):
    '''
    Sequencer generator to generate measures from dnb tracks.
    Randomly chooses amplitude, drums, and other parameters every few measures.
    '''
    amp = 1.0
    hat_sound = CLOSED_HI_HAT
    snare_sound = SNARE
    snare_sounds = choose(
        items=[SNARE, ACOUSTIC_SNARE, SIDE_STICK], weights=[0.4, 0.4, 0.2])
    num_chords = 3
    chords = ElectricPiano1
    play_chords = True
    for measure in range(measures):
        # Change parameters after a few measures
        if measure > 0 and measure % 4 == 0:
            hat_sound = pick(CLOSED_HI_HAT, OPEN_HI_HAT, RIDE1, RIDE2, COWBELL)
            snare_sound = next(snare_sounds)
            num_chords = pick(2, 3, 4)
            chords = pick(ElectricPiano1, ElectricPiano2)
            amp = between(0.8, 1)
            play_chords = odds(0.8)

        if measure == measures - 1:
            amp = 1.0

        # Add to score
        score.compose(dnb_hi_hat(score, tempo, amp, hat_sound))
        score.compose(dnb_drums(score, tempo, amp, snare_sound))
        score.compose(dnb_ghost_notes(score, tempo, amp))
        if play_chords:
            score.compose(dnb_chords(score, tempo, 48, 64,
                      num_chords, amp - 0.2, chords))
        yield intempo(8, tempo)


if __name__ == '__main__':
    tempo = 170
    track0 = MidiFile.metatrack(
        ins={0: ElectricPiano1, 1: ElectricBass_finger, 2: ElectricPiano2})

    score = Score(out=Seq())

    score.compose(dnb_track(score, 16, tempo))
    file = MidiFile("dnb.mid", [track0, score.out]).write()
