from phrases import Note, get_even_unaccented_notes
from .duyug_cr_12 import OPENING_PHRASE_1, OPENING_PHRASE_2

# Subunits
OPENING_SUBUNIT_1 = get_even_unaccented_notes([(3,2), (3,2)])
OPENING_SUBUNIT_2 = get_even_unaccented_notes([(3,1), (3,1)])
OPENING_SUBUNIT_3 = [
  ((3,1), 1/2, False),
  ((3,1), 1/4, False),
  (0, 1/8, False),
  ((3,1), 1/8, False),
]

OPENING_PHRASE_3 = OPENING_SUBUNIT_1 * 2
OPENING_PHRASE_4 = OPENING_SUBUNIT_2 * 2
OPENING_PHRASE_5 = OPENING_SUBUNIT_2 + OPENING_SUBUNIT_3

# Opening
DUYUG_CR_13_OPENING = OPENING_PHRASE_1 + OPENING_PHRASE_2 + \
  2*OPENING_PHRASE_3 + OPENING_PHRASE_4 + OPENING_PHRASE_5

# Phrases

# Composition