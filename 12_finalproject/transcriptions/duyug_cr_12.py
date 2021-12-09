from phrases import Note

def get_even_unaccented_notes(gong_nums: list[int]):
    return [(x, 1/(len(gong_nums)), False) for x in gong_nums]

# Opening
OPENING_PHRASE_1: list[Note] = [
    (0, 1/4, False),
    (3, 1/4, False),
    (3, 1/2, False),

    (3, 1/2, False),
    (3, 1/2, False),
]

OPENING_PHRASE_2: list[Note] = [
    (3, 1/2, False)
] * 4

# Subunits
SUBUNIT_443: list[Note] = [
    (4, 1/4, False),
    (4, 1/4, False),
    (3, 1/2, False),
]

SUBUNIT_4335: list[Note] = get_even_unaccented_notes([4,3,3,5])

SUBUNIT_4435: list[Note] = get_even_unaccented_notes([4,4,3,5])

SUBUNIT_55_5: list[Note] = get_even_unaccented_notes([5,5,0,5])

SUBUNIT_43: list[Note] = get_even_unaccented_notes([4,3])

SUBUNIT_65_5: list[Note] = get_even_unaccented_notes([6,5,0,5])

SUBUNIT_5677: list[Note] = get_even_unaccented_notes([5,6,7,7])

SUBUNIT_755765: list[Note] = [
    (7, 1/4, False),
    (5, 1/8, False),
    (5, 1/8, False),
    ((7, 6), 1/4, False),
    (5, 1/4, False)
]

SUBUNIT_6788: list[Note] = get_even_unaccented_notes([6,7,8,8])

SUBUNIT_88_8_8: list[Note] = [
    (8, 1/8, False),
    (8, 3/8, False),
    (8, 1/4, False),
    (0, 1/8, False),
    (8, 1/8, False),
]

SUBUNIT_8_888: list[Note] = [
    (8, 1/4, False),
    (0, 1/8, False),
    (8, 1/8, False),
    (8, 1/4, False),
    (8, 1/4, False),
]

SUBUNIT_7_67: list[Note] = [
    (7, 1/4, False),
    (0, 1/8, False),
    (6, 1/8, False),
    (7, 1/2, False),
]

SUBUNIT_88_8_7: list[Note] = [
    (8, 1/8, False),
    (8, 3/8, False),
    (8, 1/4, False),
    (7, 1/4, False),
]

SUBUNIT_567: list[Note] = [
    (5, 1/4, False),
    (6, 1/4, False),
    (7, 1/2, False),
]

SUBUNIT_6_75: list[Note] = [
    (6, 1/2, False),
    (7, 1/4, False),
    (5, 1/4, False),
]

SUBUNIT_55_5A: list[Note] = [
    (5, 1/4, False),
    (5, 1/4, True),
    (0, 1/4, False),
    (5, 1/4, False),
]

SUBUNIT_4_35: list[Note] = [
    (4, 1/2, False),
    (3, 1/4, False),
    (5, 1/4, False),
]

SUBUNIT_5557: list[Note] = get_even_unaccented_notes([5,5,5,7])

SUBUNIT_67_65: list[Note] = [
    (6, 1/8, False),
    (7, 3/8, False),
    (6, 1/4, False),
    (5, 1/4, False),
]

SUBUNIT_3355: list[Note] = get_even_unaccented_notes([3,3,5,5])

SUBUNIT_7_766: list[Note] = [
    (7, 1/2, False),
    (7, 1/4, False),
    (6, 1/8, False),
    (6, 1/8, False)
]

SUBUNIT_4554: list[Note] = get_even_unaccented_notes([4,5,5,4])

SUBUNIT_33: list[Note] = get_even_unaccented_notes([3,3])

SUBUNIT_44_3: list[Note] = [
    (4, 1/8, False),
    (4, 3/8, False),
    (3, 1/2, False),
]


# Phrases
PHRASE_1: list[Note] = get_even_unaccented_notes([4,3,0,5]) + SUBUNIT_443

PHRASE_2: list[Note] = SUBUNIT_4335 + SUBUNIT_443

PHRASE_3: list[Note] = SUBUNIT_4335 + get_even_unaccented_notes([4,4,3,3])

PHRASE_4: list[Note] = SUBUNIT_55_5 + SUBUNIT_43

PHRASE_5: list[Note] = SUBUNIT_55_5 + SUBUNIT_4435

PHRASE_6: list[Note] = SUBUNIT_65_5 + SUBUNIT_43

DOUBLE_PHRASE_1: list[Note] = PHRASE_5 + PHRASE_6

PHRASE_7: list[Note] = SUBUNIT_5677 + [
    (7, 1/4, False),
    (7, 1/8, False),
    (6, 1/8, False),
    (5, 1/2, False)
]

PHRASE_8: list[Note] = [
    (6, 1/4, False),
    (5, 1/4, True),
    (0, 1/4, False),
    (5, 1/4, False),
] + SUBUNIT_43

PHRASE_9: list[Note] = SUBUNIT_5677 + get_even_unaccented_notes([7, 7])

PHRASE_10: list[Note] = SUBUNIT_65_5 + SUBUNIT_43

DOUBLE_PHRASE_2: list[Note] = PHRASE_9 + PHRASE_10

PHRASE_11: list[Note] = get_even_unaccented_notes([5,6,7,8]) + SUBUNIT_755765

PHRASE_12: list[Note] = SUBUNIT_65_5 + SUBUNIT_43

PHRASE_13: list[Note] = get_even_unaccented_notes([5,6,7,7]) + SUBUNIT_755765

PHRASE_14: list[Note] = SUBUNIT_6788 + SUBUNIT_755765

PHRASE_15: list[Note] = get_even_unaccented_notes([6,7,8,7]) + SUBUNIT_755765

PHRASE_16: list[Note] = SUBUNIT_6788 + SUBUNIT_88_8_8

PHRASE_17: list[Note] = SUBUNIT_8_888 + SUBUNIT_7_67

PHRASE_18: list[Note] = SUBUNIT_8_888 + SUBUNIT_755765

PHRASE_19: list[Note] = SUBUNIT_6788 + SUBUNIT_88_8_7

PHRASE_20: list[Note] = get_even_unaccented_notes([6,7,8,6]) + SUBUNIT_755765

PHRASE_21: list[Note] = SUBUNIT_567 + SUBUNIT_6_75

PHRASE_22: list[Note] = SUBUNIT_55_5A + SUBUNIT_43

PHRASE_23: list[Note] = SUBUNIT_55_5A + SUBUNIT_4_35

PHRASE_24: list[Note] = SUBUNIT_5557 + SUBUNIT_67_65

PHRASE_25: list[Note] = SUBUNIT_3355 + SUBUNIT_43

PHRASE_26: list[Note] = SUBUNIT_5677 + SUBUNIT_7_766

PHRASE_27: list[Note] = SUBUNIT_4554 + SUBUNIT_33

PHRASE_28: list[Note] = SUBUNIT_3355 + SUBUNIT_44_3

# Composition
DUYUG_CR_12: list[Note] = \
    OPENING_PHRASE_1 + 5*OPENING_PHRASE_2 + \
    2*PHRASE_1 + PHRASE_2 + \
    PHRASE_3 + 4*PHRASE_4 + \
        2*DOUBLE_PHRASE_1 + PHRASE_7 + PHRASE_8 + \
                            2*DOUBLE_PHRASE_2 + \
                            PHRASE_11 + PHRASE_12 + \
                            PHRASE_13 + \
                            PHRASE_14 + \
                            PHRASE_15 + \
                                            PHRASE_16 + PHRASE_17 + \
                                            PHRASE_16 + PHRASE_18 + \
                                            PHRASE_19 + \
                            4*PHRASE_20 + PHRASE_8 + \
                            PHRASE_21 + PHRASE_8 + \
        2*PHRASE_22 + \
        PHRASE_23 + PHRASE_10 + \
                            PHRASE_24 + PHRASE_25 + \
                            PHRASE_26 + PHRASE_27 + \
                            PHRASE_24 + PHRASE_28

