from phrases import Note, get_even_unaccented_notes

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

SUBUNIT_655_5: list[Note] = [
    (6, 1/4, False),
    (5, 1/8, False),
    (5, 1/8, False),
    (0, 1/4, False),
    (5, 1/4, False),
]

SUBUNIT_556: list[Note] = [
    (5, 1/4, False),
    (5, 1/4, False),
    (6, 1/2, False),
]

SUBUNIT_67: list[Note] = get_even_unaccented_notes([6,7])

SUBUNIT_4422: list[Note] = get_even_unaccented_notes([4,4,2,2])

SUBUNIT_4566: list[Note] = get_even_unaccented_notes([4,5,6,6])

SUBUNIT_5543: list[Note] = get_even_unaccented_notes([5,5,4,3])

SUBUNIT_5654: list[Note] = get_even_unaccented_notes([5,6,5,4])

SUBUNIT_5422: list[Note] = get_even_unaccented_notes([5,4,4,2])

SUBUNIT_4256: list[Note] = get_even_unaccented_notes([0,(4,2),5,6])

SUBUNIT_55544: list[Note] = get_even_unaccented_notes([5,5,(5,4),4])

SUBUNIT_56542: list[Note] = get_even_unaccented_notes([5,6,5,(4,2)])

SUBUNIT_52522: list[Note] = get_even_unaccented_notes([(5,2),5,2,2])

SUBUNIT_41541: list[Note] = get_even_unaccented_notes([0, (4,1), 5, (4,1)])

SUBUNIT_61_4242: list[Note] = [
    ((6,1), 1/2, False),
    ((4,2), 1/4, False),
    ((4,2), 1/4, False),
]

SUBUNIT_51451: list[Note] = get_even_unaccented_notes([0, (5,1), 4, (5,1)])

SUBUNIT_5143232: list[Note] = get_even_unaccented_notes([(5,1), 4, (3,2), (3,2)])

SUBUNIT_3234: list[Note] = [
    ((3,2), 1/2, False),
    (3, 1/4, False),
    (4, 1/4, False),
]

SUBUNIT_5243233: list[Note] = [
    ((5,2), 1/4, False),
    (4, 1/4, False),
    ((3,2), 1/4, False),
    (3, 1/8, False),
    (3, 1/8, False),
]

SUBUNIT_1234: list[Note] = get_even_unaccented_notes([1,2,3,4])

SUBUNIT_56777: list[Note] = [
    (5, 1/4, False),
    (6, 1/4, False),
    (7, 1/4, False),
    (7, 1/8, False),
    (7, 1/8, False),
]

SUBUNIT_7654 = get_even_unaccented_notes([7,6,5,4])

SUBUNIT_5554 = get_even_unaccented_notes([5,5,5,4])

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

PHRASE_29: list[Note] = SUBUNIT_655_5 + SUBUNIT_43

PHRASE_30: list[Note] = SUBUNIT_556 + SUBUNIT_67

PHRASE_31: list[Note] = SUBUNIT_65_5 + SUBUNIT_4_35

PHRASE_32: list[Note] = SUBUNIT_65_5 + SUBUNIT_4422

PHRASE_33: list[Note] = SUBUNIT_4566 + SUBUNIT_5543

PHRASE_34: list[Note] = SUBUNIT_5654 + SUBUNIT_5422

PHRASE_35: list[Note] = SUBUNIT_4256 + SUBUNIT_55544

PHRASE_36: list[Note] = SUBUNIT_56542 + SUBUNIT_52522

PHRASE_37: list[Note] = SUBUNIT_41541 + SUBUNIT_61_4242

PHRASE_38: list[Note] = SUBUNIT_51451 + SUBUNIT_5143232

PHRASE_39: list[Note] = SUBUNIT_3234 + SUBUNIT_5243233

PHRASE_40: list[Note] = SUBUNIT_1234 + SUBUNIT_5243233

CLOSING_PHRASE_1: list[Note] = SUBUNIT_1234 + SUBUNIT_56777

CLOSING_PHRASE_2: list[Note] = SUBUNIT_7654 + SUBUNIT_5554

FINAL: list[Note] = [(3, 1, True)]


# Composition
DUYUG_CR_12_BODY = \
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
                            PHRASE_24 + PHRASE_28 + \
                PHRASE_29 + \
    PHRASE_23 + PHRASE_29 + PHRASE_30 + PHRASE_31 + \
                                        PHRASE_32 + \
    PHRASE_33 + PHRASE_34 + PHRASE_35 + PHRASE_36 + \
    PHRASE_37 + 2*PHRASE_38 + PHRASE_39 + PHRASE_40

DUYUG_CR_12_OPENING: list[Note] = OPENING_PHRASE_1 + 5*OPENING_PHRASE_2

DUYUG_CR_12_CLOSING: list[Note] = CLOSING_PHRASE_1 + CLOSING_PHRASE_2 + FINAL

DUYUG_CR_12: list[Note] = DUYUG_CR_12_OPENING + DUYUG_CR_12_BODY + DUYUG_CR_12_CLOSING