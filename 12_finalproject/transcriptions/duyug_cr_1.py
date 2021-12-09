from phrases import Note

# Opening
DUYUG_CR_1_OPENING: list[Note] = [
    (3, 1/2, False)
] * 4

# Subunits
SUBUNIT_1 = [
    ((4, 1), 1/4, False),
    (1, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False)
]

SUBUNIT_2 = [
    (3, 1/2, False),
    (2, 1/4, False),
    (2, 1/4, False)
]

SUBUNIT_3 = [
    (3, 1/4, False),
    (2, 1/4, False),
    (3, 1/4, False),
    ((4, 3), 1/4, False),
]

# Phrases
BODY_1: list[Note] = SUBUNIT_1 + SUBUNIT_2

BODY_2: list[Note] = [
    (5, 1/4, False),
    (4, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False),
] + SUBUNIT_2

BODY_3: list[Note] = SUBUNIT_3 + SUBUNIT_2

CLOSING: list[Note] = SUBUNIT_3 + [
    (5, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False),
    ((4, 3), 1/4, False),
]

FINAL_NOTE: list[Note] = [
    (5, 1, True)
]

# Composition
DUYUG_CR_1_BODY = BODY_1*3 + BODY_2*3 + BODY_1*3 + BODY_3*3
DUYUG_CR_1_CLOSING = CLOSING + FINAL_NOTE
DUYUG_CR_1 = DUYUG_CR_1_OPENING + DUYUG_CR_1_BODY + DUYUG_CR_1_CLOSING
