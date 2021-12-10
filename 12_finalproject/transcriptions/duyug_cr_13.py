from phrases import get_even_unaccented_notes
from .duyug_cr_12 import OPENING_PHRASE_1, OPENING_PHRASE_2

# Subunits
OPENING_SUBUNIT_1 = get_even_unaccented_notes([(3, 2), (3, 2)])
OPENING_SUBUNIT_2 = get_even_unaccented_notes([(3, 1), (3, 1)])
OPENING_SUBUNIT_3 = [
    ((3, 1), 1/2, False),
    ((3, 1), 1/4, False),
    (0, 1/8, False),
    ((3, 1), 1/8, False),
]

SUBUNIT_313342 = get_even_unaccented_notes([(3, 1), 3, 3, (4, 2)])

SUBUNIT_314313 = [
    ((3, 1), 1/4, False),
    (4, 1/4, False),
    ((3, 1), 1/4, False),
    (0, 1/8, False),
    (3, 1/8, False),
]

SUBUNIT_314314 = [
    ((3, 1), 1/4, False),
    (4, 1/4, False),
    ((3, 1), 1/4, False),
    (0, 1/8, False),
    (4, 1/8, False),
]

SUBUNIT_4231442 = get_even_unaccented_notes([(4, 2), (3, 1), 4, (4, 2)])

SUBUNIT_3152452 = get_even_unaccented_notes([(3, 1), (5, 2), 4, (5, 2)])

SUBUNIT_415626 = get_even_unaccented_notes([(4, 1), 5, (6, 2), 6])

SUBUNIT_251452 = get_even_unaccented_notes([2, (5, 1), 4, (5, 2)])

SUBUNIT_415625 = get_even_unaccented_notes([(4, 1), 5, (6, 2), 5])

SUBUNIT_6251452 = get_even_unaccented_notes([(6,2), (5, 1), 4, (5, 2)])

SUBUNIT_41562_6 = [
    ((4,1), 1/4, False),
    (5, 1/4, False),
    ((6,2), 1/4, False),
    (0, 1/8, False),
    (6, 1/8, False),
]

SUBUNIT_41562_7 = [
    ((4,1), 1/4, False),
    (5, 1/4, False),
    ((6,2), 1/4, False),
    (0, 1/8, False),
    (7, 1/8, False),
]

SUBUNIT_456_5 = [
    (4, 1/4, False),
    (5, 1/4, False),
    (6, 1/4, False),
    (0, 1/8, False),
    (5, 1/8, False),
]

SUBUNIT_41562_5 = [
    ((4,1), 1/4, False),
    (5, 1/4, False),
    ((6,2), 1/4, False),
    (0, 1/8, False),
    (5, 1/8, False),
]

SUBUNIT_3145141 = get_even_unaccented_notes([(3,1), 4, (5,1), (4,1)])

SUBUNIT_342341 = get_even_unaccented_notes([3, (4,2), 3, (4,1)])

SUBUNIT_5143242 = get_even_unaccented_notes([(5,1), 4, (3,2), (4,2)])

SUBUNIT_341514 = get_even_unaccented_notes([3, (4,1), (5,1), 4])




# Phrases
OPENING_PHRASE_3 = OPENING_SUBUNIT_1 * 2
OPENING_PHRASE_4 = OPENING_SUBUNIT_2 * 2
OPENING_PHRASE_5 = OPENING_SUBUNIT_2 + OPENING_SUBUNIT_3

PHRASE_1 = SUBUNIT_313342 + SUBUNIT_314313

PHRASE_2 = SUBUNIT_313342 + SUBUNIT_314314

PHRASE_3 = SUBUNIT_4231442 + SUBUNIT_314313

PHRASE_4 = SUBUNIT_3152452 + SUBUNIT_314313

PHRASE_5 = SUBUNIT_3152452 + SUBUNIT_415626

PHRASE_6 = SUBUNIT_251452 + SUBUNIT_314313

PHRASE_7 = SUBUNIT_3152452 + SUBUNIT_415625

PHRASE_8 = SUBUNIT_6251452 + SUBUNIT_314313

PHRASE_9 = SUBUNIT_3152452 + SUBUNIT_41562_6

PHRASE_10 = SUBUNIT_6251452 + SUBUNIT_41562_6

PHRASE_11 = SUBUNIT_6251452 + SUBUNIT_41562_7

PHRASE_12 = SUBUNIT_3152452 + SUBUNIT_456_5

PHRASE_13 = SUBUNIT_3152452 + SUBUNIT_41562_7

PHRASE_14 = SUBUNIT_3152452 + SUBUNIT_41562_5

PHRASE_15 = SUBUNIT_6251452 + SUBUNIT_41562_5

PHRASE_16 = SUBUNIT_3152452 + SUBUNIT_3145141

PHRASE_17 = SUBUNIT_342341 + SUBUNIT_5143242

PHRASE_18 = SUBUNIT_3145141 + SUBUNIT_5143242

# Opening
DUYUG_CR_13_OPENING = OPENING_PHRASE_1 + OPENING_PHRASE_2 + \
    2*OPENING_PHRASE_3 + OPENING_PHRASE_4 + OPENING_PHRASE_5

DUYUG_CR_13_BODY = \
    2*PHRASE_1 + \
    PHRASE_2 + PHRASE_3 + \
    2*PHRASE_1 + 4*PHRASE_4 + PHRASE_5 + \
                PHRASE_6 + PHRASE_7 + \
                PHRASE_8 + PHRASE_9 + PHRASE_10 + \
                                    3*PHRASE_11 + \
                PHRASE_8 + PHRASE_12 + \
                PHRASE_8 + PHRASE_13 + PHRASE_11 + \
                PHRASE_8 + \
                6*PHRASE_4 + PHRASE_14 + PHRASE_15 + \
                                        2*PHRASE_11 + \
                PHRASE_8 + PHRASE_14 + \
                PHRASE_8 + \
                3*PHRASE_4 + \
    PHRASE_16 + PHRASE_17 + PHRASE_18


# Closing
CLOSING_SUBUNIT_3233 = get_even_unaccented_notes([3,2,3,3])
CLOSING_SUBUNIT_5677 = get_even_unaccented_notes([5,6,7,7])
CLOSING_SUBUNIT_56553 = get_even_unaccented_notes([5,(6,5),5,3])
CLOSING_SUBUNIT_5665 = get_even_unaccented_notes([5,6,6,5])

CLOSING_PHRASE_1 = CLOSING_SUBUNIT_3233 + CLOSING_SUBUNIT_5677
CLOSING_PHRASE_2 = CLOSING_SUBUNIT_56553 + CLOSING_SUBUNIT_5665

FINAL_NOTE = get_even_unaccented_notes([3])

DUYUG_CR_13_CLOSING = CLOSING_PHRASE_1 + CLOSING_PHRASE_2 + FINAL_NOTE


# Composition
DUYUG_CR_13 = DUYUG_CR_13_OPENING + DUYUG_CR_13_BODY + DUYUG_CR_13_CLOSING
