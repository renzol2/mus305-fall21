from phrases import Note

# Opening
DUYUG_CR_1_OPENING: list[Note] = [
    (3, 1/2, False)
] * 4

# Submodules
DUYUG_CR_1_SUBMODULE_1 = [
    ((4, 1), 1/4, False),
    (1, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False)
]

DUYUG_CR_1_SUBMODULE_2 = [
    (3, 1/2, False),
    (2, 1/4, False),
    (2, 1/4, False)
]

DUYUG_CR_1_SUBMODULE_3 = [
    (3, 1/4, False),
    (2, 1/4, False),
    (3, 1/4, False),
    ((4, 3), 1/4, False),
]

# Phrases
DUYUG_CR_1_BODY_1: list[Note] = DUYUG_CR_1_SUBMODULE_1 + DUYUG_CR_1_SUBMODULE_2

DUYUG_CR_1_BODY_2: list[Note] = [
    (5, 1/4, False),
    (4, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False),
] + DUYUG_CR_1_SUBMODULE_2

DUYUG_CR_1_BODY_3: list[Note] = DUYUG_CR_1_SUBMODULE_3 + DUYUG_CR_1_SUBMODULE_2

DUYUG_CR_1_CLOSING: list[Note] = DUYUG_CR_1_SUBMODULE_3 + [
    (5, 1/4, False),
    (5, 1/4, False),
    (3, 1/4, False),
    ((4, 3), 1/4, False),
]

DUYUG_CR_1_FINAL_NOTE: list[Note] = [
    (5, 1, True)
]

# Composition
DUYUG_CR_1 = DUYUG_CR_1_OPENING + DUYUG_CR_1_BODY_1*3 + DUYUG_CR_1_BODY_2*3 + \
    DUYUG_CR_1_BODY_1*3 + DUYUG_CR_1_BODY_3 * \
    3 + DUYUG_CR_1_CLOSING + DUYUG_CR_1_FINAL_NOTE
