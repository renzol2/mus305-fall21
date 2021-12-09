from phrases import Note, get_even_unaccented_notes
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

# Opening
DUYUG_CR_13_OPENING = OPENING_PHRASE_1 + OPENING_PHRASE_2 + \
    2*OPENING_PHRASE_3 + OPENING_PHRASE_4 + OPENING_PHRASE_5

DUYUG_CR_13_BODY = \
    2*PHRASE_1 + \
    PHRASE_2 + PHRASE_3 + \
    2*PHRASE_1 + 4*PHRASE_4 + PHRASE_5 + \
                    PHRASE_6 + PHRASE_7 + \
                    PHRASE_8 + PHRASE_9 + PHRASE_10 + \
                                        3*PHRASE_11

# Composition
DUYUG_CR_13 = DUYUG_CR_13_OPENING + DUYUG_CR_13_BODY
