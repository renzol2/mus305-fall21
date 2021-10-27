import musx
from musx import Interval
from musx.midi.gm import ElectricGuitar_clean, Marimba, PizzicatoStrings, Xylophone
from musx.ran import beta, between, brown, odds, uniran


def gamecube(q, envelope: list, num_notes: int, min_key: int, max_key: int, rhy: float, chord_intervals=[], chord_chance=0.2):
    play_strings = True
    for i in range(num_notes):
        x = musx.rescale(i, 0, num_notes, 0, 1)  # get position in composition
        y = musx.interp(x, envelope)  # get mapped x value from envelope

        # Take y and convert to keynum based on arguments
        min_env_val, max_env_val = min(envelope), max(envelope)
        key = musx.rescale(y, min_env_val, max_env_val, min_key, max_key)

        # Create chord
        dur = 0.25
        amp = 0.8
        root_pitch = musx.Pitch.from_keynum(int(key))

        # Add marimba
        marimba = musx.Note(time=q.now, duration=dur,
                            pitch=root_pitch.keynum(), amplitude=amp, instrument=0)
        q.add(marimba)

        # Add strings, if necessary
        if play_strings:
            if odds(chord_chance):
                pitches = [root_pitch] + \
                    [i.transpose(root_pitch) for i in chord_intervals]
                for p in pitches:
                    pizz = musx.Note(time=q.now, duration=dur,
                                     pitch=p.keynum(), amplitude=amp, instrument=1)
                    q.add(pizz)
            else:
                q.add(musx.Note(time=q.now, duration=dur, pitch=root_pitch.keynum(
                ) + between(-5, 5), amplitude=amp, instrument=1))
        play_strings = not play_strings
        yield rhy
    
    # Play hit at the end
    pitches = [root_pitch] + \
                    [i.transpose(root_pitch) for i in chord_intervals]
    for p in pitches:
        pizz = musx.Note(time=q.now, duration=dur,
                            pitch=p.keynum(), amplitude=amp, instrument=1)
        q.add(pizz)


sequence = musx.Seq()
envelope_score = musx.Score(sequence)
ENV_LENGTH = 20
envelope = [round(uniran(), 2) for _ in range(ENV_LENGTH)]
print(envelope)
num_notes = 70
min_key, max_key = 40, 100
rhy = 0.12

envelope_score.compose([0, gamecube(envelope_score, envelope, num_notes, min_key, max_key, rhy, [
    Interval('M3'), Interval('P5'), Interval('M7')
])])
track0 = musx.MidiFile.metatrack(ins={0: Marimba, 1: PizzicatoStrings})
env_file = musx.MidiFile("gamecube.mid", [track0, sequence]).write()
print('OK!')
