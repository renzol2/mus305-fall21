import musx
from musx.gens import choose, cycle, markov_analyze
from musx.interval import Interval
from musx.midi.gm import AcousticBass, AcousticGrandPiano, AcousticSnare, BassDrum1, ClosedHiHat, Cowbell, CrashCymbal1, ElectricBass_finger, ElectricGuitar_jazz, ElectricPiano1, ElectricPiano2, ElectricSnare, OpenHiHat, RideCymbal1, RideCymbal2, SideStick, ElectricGuitar_clean
from musx.midi.midifile import MidiFile
from musx.note import Note
from musx.pitch import Pitch
from musx.ran import between, odds, pick
from musx.rhythm import intempo
from musx.score import Score
from musx.seq import Seq

CRASH = CrashCymbal1 + 1
CLOSED_HI_HAT = ClosedHiHat + 1
OPEN_HI_HAT = OpenHiHat + 1
RIDE1 = RideCymbal1 + 1
RIDE2 = RideCymbal2 + 1
COWBELL = Cowbell + 1
SNARE = ElectricSnare + 1
ACOUSTIC_SNARE = AcousticSnare + 1
SIDE_STICK = SideStick + 1
KICK = BassDrum1 + 1
KICK_OR_REST = 'kick or rest'
SNARE_OR_REST = 'snare or rest'
REST = 'r'

'''

Markov for main guitar riff
- transcribe riff from some song
- use markov_analyze

Markov for chords
- just uhh choose chords from the same song as riff
- get chord progression, use markov_analyze

Markov for drums?
- 

Markov to change time signatures of each measure
- Possible measure values
  - 3/4
  - 4/4
  - 5/4
  - 5/8
  - 7/8
- maybe pick 4 measure values and loop through them 4x for a total of 16

Markov for sections?
- just riff
- drums + riff
- riff + bass
- drums + riff + bass

'''

CHINCHILLA_KEYS = [
    'B3', 'C4', 'A3', 'F4', 'G4', 'E4', 'C4', 'C4', 'C5', 'A4', 'G4', 'A4', 'E4', 'C4', 'E4', 'C4', 'G4', 'E4', 'C4', 'D4', 'E4', 'C4', 'G4'
]
CHINCHILLA_RHYS = [
    0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
]

never_meant = [
    (None, 0.5),
    (Pitch('E4'), 0.25),
    (Pitch('D4'), 0.25),
    (Pitch('C4'), 0.5),
    (Pitch('G3'), 0.5),
    (Pitch('A3'), 2),
    (Pitch('B3'), 1.5),
    (Pitch('C4'), 0.5),
    (Pitch('D4'), 2),
    (Pitch('E4'), 1.5),
    (Pitch('F4'), 0.5),
    (Pitch('G4'), 2),

    # Extra notes
    (Pitch('B4'), 0.5),
    (Pitch('C5'), 0.5),
    (Pitch('B4'), 0.5),
]

NEVER_MEANT_KEYNUMS = [
    p.keynum() if p is not None else None for p, _ in never_meant]
NEVER_MEANT_RHYS = [r for _, r in never_meant]


def generate_riff(score: Score, note_rules: dict, rhythm_rules: dict, tempo: int, reps: int, dur: float):
    note_pat = musx.markov(note_rules)
    rhythm_pat = musx.markov(rhythm_rules)
    for _ in range(reps):
        next_note = next(note_pat)
        if next_note:
            score.add(musx.Note(time=score.now, pitch=next_note, duration=dur))
        yield intempo(next(rhythm_pat), tempo)


def generate_set_riff(note_rules: dict, rhythm_rules: dict, reps: int):
    note_pat = musx.markov(note_rules)
    rhythm_pat = musx.markov(rhythm_rules)
    return [(next(note_pat), next(rhythm_pat)) for _ in range(reps)]

def generate_pattern(original_pattern: list, order: int = between(1, 4)):
    rules = markov_analyze(original_pattern, order)
    gen = musx.markov(rules)
    return [next(gen) for _ in range(len(original_pattern))]

def compose_hi_hat(score: Score, tempo: int, ampl: float, sound: int = CLOSED_HI_HAT):
    '''
    Generates hi-hats on eighth notes with alternating accents.
    Can substitute closed hi-hat for other sounds.
    '''
    rhy = intempo(0.5, tempo)
    dur = intempo(0.5, tempo)
    acc_amp = 0.8
    non_acc_amp = 0.3

    # >   >     >   >     >   >     > > >
    # + + + + | + + + + | + + + + | + o + +
    hi_hat_pattern = [
        CRASH, CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT,
        CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT, OPEN_HI_HAT,
        CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT,
        CLOSED_HI_HAT, OPEN_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT,
        CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT, OPEN_HI_HAT,
        CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT, CLOSED_HI_HAT,
    ]
    
    hi_hat_pattern = generate_pattern(hi_hat_pattern)

    pat = cycle(hi_hat_pattern)
    for i in range(len(hi_hat_pattern)):
        k = next(pat)

        # Accent every other note and open hi-hat
        amp = acc_amp if k == OPEN_HI_HAT or i % 2 == 0 else non_acc_amp

        m = Note(time=score.now, duration=dur, pitch=k,
                 amplitude=ampl * amp, instrument=9)
        score.add(m)
        yield rhy


def compose_kick_snare(score: Score, tempo: int, ampl: float, snare_sound: int = SNARE):
    '''
    Generates random kick & snare patterns.
    '''
    rhy = intempo(0.5, tempo)
    dur = intempo(0.2, tempo)
    amp = 0.95

    bass_or_rest = choose(items=[KICK, REST], weights=[0.25, 0.75])

    # eighth notes
    # b=bass, s=snare, .=rest, ?=bass or rest
    # . . s . . . s . | . . s . . . s .
    # b . . . . b . . | ? ? . ? ? ? . ?
    kick_snare_pattern = [
        KICK, REST, REST, KICK,
        SNARE, REST, REST, KICK,
        REST, KICK, SNARE, REST,
        REST, KICK, REST, KICK,
        SNARE, REST, REST, KICK,
        REST, KICK, SNARE, REST
    ]

    kick_snare_pattern = generate_pattern(kick_snare_pattern)

    pat = cycle(kick_snare_pattern)
    for _ in range(len(kick_snare_pattern)):
        k = next(pat)

        # Choose bass drum or rest if noted
        pitch = k
        if pitch == KICK_OR_REST:
            pitch = next(bass_or_rest)

        if pitch != REST:
            m = Note(time=score.now, duration=dur, pitch=pitch,
                     amplitude=ampl * amp, instrument=9)
            score.add(m)
        yield rhy


def compose_riff(score: Score, riff: list[tuple[int, float]], tempo: int, amp: float, dur: float):
    for keynum, rhy in riff:
        if keynum is not None:
            m = Note(time=score.now, duration=dur, pitch=keynum,
                     amplitude=amp)
            score.add(m)
        yield intempo(rhy, tempo)


def compose_second_guitar(score: Score, tempo: int, amp: float, dur: float):
    notes = [None, 'C4', 'E4', 'C4']
    pattern = [None]*4 + notes*5
    pitch_pattern = [
        Pitch(note) if note is not None else None for note in pattern]

    for p in pitch_pattern:
        if p is not None:
            m = Note(time=score.now, duration=dur, pitch=p.keynum(),
                     amplitude=amp, instrument=2)
            score.add(m)
        yield intempo(0.5, tempo)


def compose_bass(score: Score, tempo: int, amp: float, reps: int):
    chords = [4, 5, 6, 5, 4, 1, 4]
    pitch_map = {
        1: Pitch('C2'),
        4: Pitch('F2'),
        5: Pitch('G2'),
        6: Pitch('A2'),
    }
    bass_rules = markov_analyze(chords, between(1, 5))
    pat = musx.markov(bass_rules)
    on_down_beat = True
    down_beat_length = 4.5
    off_beat_length = 1.5
    for _ in range(reps):
        length = down_beat_length if on_down_beat else off_beat_length
        score.add(musx.Note(time=score.now, pitch=pitch_map[next(pat)].keynum(),
                  duration=intempo(length, tempo), amplitude=amp, instrument=1))
        yield intempo(length, tempo)
        on_down_beat = not on_down_beat


def create_mathrock(score: Score, measures: int, tempo: int, keynums: list, rhythms: list):
    # Compose riff
    num_notes = 24
    note_rules = markov_analyze(riff_keynums, 1)
    rhythm_rules = markov_analyze(riff_rhythms, 3)
    riff = generate_set_riff(note_rules, rhythm_rules, num_notes)
    for measure in range(measures):
        score.compose(compose_riff(score, riff, tempo, 0.8, 0.25))
        score.compose(compose_second_guitar(score, tempo, 0.4, 0.25))
        score.compose(compose_bass(score, tempo, 0.8, 4))
        score.compose(compose_hi_hat(score, tempo, 1.0))
        score.compose(compose_kick_snare(score, tempo, 1.0))
        yield intempo(12, tempo)


if __name__ == '__main__':
    riff_keynums = [Pitch(note).keynum() for note in CHINCHILLA_KEYS]
    riff_rhythms = NEVER_MEANT_RHYS
    tempo = 144
    track0 = MidiFile.metatrack(
        ins={0: ElectricGuitar_clean, 1: ElectricBass_finger, 2: ElectricGuitar_jazz})

    score = Score(out=Seq())

    score.compose(create_mathrock(score, 8, tempo, riff_keynums, riff_rhythms))
    file = MidiFile("mathrock.mid", [track0, score.out]).write()
