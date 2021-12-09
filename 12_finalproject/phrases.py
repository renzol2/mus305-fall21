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
