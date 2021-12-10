from typing import Union


'''
Kulintang Phrase Structure

gong_num: 1-8, 0 = rest
single stroke 
    -> (gong_num: int, beat_length: float, accent: bool)
sabay (two)   
    -> ((gong_num_L: int, gong_num_R: int), duration: float, accent: bool)
'''

# Representation of a single kulintang note
Note = tuple[Union[int, tuple[int, int]], float, bool]


def get_even_unaccented_notes(gong_nums: list) -> list[Note]:
    '''
    Generates evenly-spaced, unaccented kulintang notes at given pitches in list
    '''
    return [(x, 1/(len(gong_nums)), False) for x in gong_nums]


DUYUG_CR_1_SAMPLE: list[Note] = [
    ((4, 1), 1/4, False),
    (1, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False),

    (3, 1/2, False),
    (2, 1/4, False),
    (2, 1/4, False)
]

DUYUG_A_BINALIG_C4_14_SAMPLE: list[Note] = [
    (1, 1/4, False),
    (1, 1/8, False),
    (1, 1/8, False),
    (2, 1/4, False),
    (2, 1/4, False),

    (1, 1/4, False),
    (2, 1/4, False),
    (3, 1/4, False),
    (2, 1/4, False)
]

# Provided by: Kristina Benitez
DUYUG_DABAKAN_SAMPLE_PATTERN: list[Note] = [
    (1, 1/4, False),
    (1, 1/8, False),
    (1, 1/8, False),
    (1, 1/4, False),
    (1, 1/4, False),
]

# Provided by: Danongan Kalanduyan nd the Palabunibunyan Kulintang Ensemble
BINALIG_DABAKAN_SAMPLE_PATTERN: list[Note] = [
    (1, 1/4, False),
    (1, 1/8, True),
    (1, 1/8, False),
    (1, 1/8, False),
    (1, 1/8, True),
    (1, 1/8, False),
    (1, 1/8, False),
    (1, 1/4, True),
    (1, 1/8, False),
    (1, 1/8, False),
    (1, 1/4, True),
    (0, 1/8, False),
    (1, 1/8, False),
]

# Provided by: Danongan Kalanduyan nd the Palabunibunyan Kulintang Ensemble
BINALIG_BABANDIR_SAMPLE_PATTERN: list[Note] = [
    (1, 1/2, True),
    (1, 1/4, False),
    (1, 1/4, False),
    (1, 1/2, False),
    (1, 1/2, False),
]

# Provided by: Kristina Benitez
DUYUG_BABANDIR_SAMPLE_PATTERN_1: list[Note] = DUYUG_DABAKAN_SAMPLE_PATTERN

# Provided by: Kristina Benitez
DUYUG_BABANDIR_SAMPLE_PATTERN_2: list[Note] = [
    (1, 1/4, True),
    (1, 1/2, False),
    (1, 1/4, False),

    (1, 1/2, False),
    (1, 1/2, False),
]

# Provided by: Kristina Benitez
DUYUG_BABANDIR_SAMPLE_PATTERN_3: list[Note] = [
    (1, 1/2, True),
    (1, 1/4, False),
    (1, 1/4, False),

    (1, 1/4, False),
    (1, 1/4, False),
    (1, 1/2, False),
]

SCALE: list[Note] = [
    (i+1, 1, False) for i in range(8)
]
