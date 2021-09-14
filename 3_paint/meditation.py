if __name__ == "__main__":
    from musx import Score, Seq, MidiFile
    from musx.midi.gm import Koto, TaikoDrum, Shamisen, OrchestralHarp, Shakuhachi
    from musx.paint import brush, spray

    MEASURE_LENGTH = 1.125

    track0 = MidiFile.metatrack(
        ins={0: Koto, 1: TaikoDrum, 2: Shamisen, 3: OrchestralHarp, 4: Shakuhachi})
    track1 = Seq()
    score = Score(out=track1)

    scale1 = [0, 1, 5, 7, 10, 12]
    perc = [10]

    SECTION_1_LENGTH = MEASURE_LENGTH * 32
    SECTION_2_LENGTH = MEASURE_LENGTH * 16

    # Lower koto
    lower_koto_start = 0
    lower_koto = brush(score, pitch=[k + 50 for k in scale1], duration=3, rhythm=[
        0.25, 0.125], amplitude=[0.3, 0.6], end=SECTION_1_LENGTH, instrument=0)

    # Higher koto
    higher_koto_start = MEASURE_LENGTH * 4
    higher_koto = spray(score, pitch=62, duration=0.6, rhythm=[
        0.125, 0.25, 0.5, 0.5], band=scale1, end=SECTION_1_LENGTH - higher_koto_start, instrument=0)

    # Taiko
    taiko_start = 0
    taiko = brush(score, pitch=perc, duration=4,
                  rhythm=[MEASURE_LENGTH], amplitude=[0.9], end=SECTION_1_LENGTH + MEASURE_LENGTH, instrument=1)

    # Shamisen
    shamisen_start = MEASURE_LENGTH * 12
    shamisen = spray(score, pitch=74, duration=1, rhythm=[
                     0.25, 0.5, 0.25, 0.125], band=scale1, end=SECTION_1_LENGTH + SECTION_2_LENGTH - shamisen_start, instrument=2)

    # Harp
    harp_start = SECTION_1_LENGTH
    harp = spray(score, pitch=74, duration=2, rhythm=[
                 0.125, 0.125, 0.25], band=scale1, end=SECTION_2_LENGTH, instrument=3)

    # Shakuhachi
    shakuhachi_start = SECTION_1_LENGTH + MEASURE_LENGTH * 4
    shakuhachi = spray(score, pitch=74, duration=4, rhythm=[
                       1, 2], band=scale1, end=SECTION_2_LENGTH - MEASURE_LENGTH * 4, instrument=4)

    score.compose([
        # Section 1
        [lower_koto_start, lower_koto],
        [taiko_start, taiko],
        [higher_koto_start, higher_koto],
        [shamisen_start, shamisen],

        # Section 2
        [harp_start, harp],
        [shakuhachi_start, shakuhachi],
    ])

    file = MidiFile('meditation.mid', [track0, track1]).write()
    print(f'Wrote "{file.pathname}"')
