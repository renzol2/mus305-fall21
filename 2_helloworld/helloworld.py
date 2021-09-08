# In this homework you will compose a short midi composition whose pitch
# (and any other sound attributes you want to include) is controlled by
# 'sonifying' python strings, where each ascii codepoint (character) in a
# string is treated as a midi key number. This works because the standard
# ascii character set (0-127) maps directly onto midi keynums =:).
# See:  https://commons.wikimedia.org/wiki/File:ASCII-Table-wide.svg

# Use this link to learn about the common musx imports listed below.
# https://musx-admin.github.io/musx/index.html
from musx import Score, Seq, Note, MidiFile, MidiEvent, rescale
from musx.midi import gm
import requests


# define a composer (generator) that will add notes to our score.
def playstring(score: Score, string: str, rhy: float, dur: float, amp: float, chan: int = 0, range: tuple = (0, 127)):
    # the builtin ord() function converts a single char into its
    # ascii code point (an integer 0-127). The builtin map() function
    # returns an iterator that will apply its first arg (a function)
    # to every element in its second arg (an iterable).
    for char in map(ord, string):
        # create a note to play each asci code point as a MIDI key number
        # with a specified onset, duration and amplitude.
        p = rescale(char, 0, 127, range[0], range[1])
        note = Note(time=score.now, duration=dur, pitch=p,
                    amplitude=amp, instrument=chan)
        # add the note at the current time in the score
        score.add(note)
        # yield back the time to wait until the composer is called again.
        yield rhy


def fetch_random_numbers(low: int, high: int, count: int) -> tuple[int]:
    '''
    Fetches a list of random integers from the random number API using the
    reddit comment feed as the seed.

    "The Idea behind this function is to generate random numbers based on 
    the 'Free Will' of people generating truly random numbers."
    http://www.randomnumberapi.com/
    '''
    text = requests.get(
        f'http://www.randomnumberapi.com/api/v1.0/randomredditnumber?min={low}&max={high}&count={count}').text
    return tuple([int(c) for c in text[1:-1].split(', ')])


if __name__ == '__main__':
    # allocate a sequence to hold our notes
    seq = Seq()

    # Possible GM instruments
    instruments = [gm.BlownBottle, gm.AcousticGuitar_nylon,
                   gm.Violin, gm.BrassSection, gm.SynthBass2, gm.Oboe, gm.Shakuhachi]

    # Choose a random number, seeded by latest comments submitted to Reddit as the seed
    NUM_INSTRUMENTS = 2
    instrument1, instrument2 = fetch_random_numbers(
        0, len(instruments) - 1, NUM_INSTRUMENTS)
    print('Instrument 1 index: ', instrument1)
    print('Instrument 2 index: ', instrument2)

    # Assign instruments
    meta = MidiFile.metatrack(ins={0: instrument1, 1: instrument2})

    # allocate a score and give it the sequence
    score = Score(out=seq)

    # Fetch a random inspirational quote
    r = requests.get(
        'https://api.forismatic.com/api/1.0/?method=getQuote&format=text&lang=en')
    quote = r.text
    print(' > ' + quote)

    # Create a random range for each instrument
    range1_a, range1_b, range2_a, range2_b = fetch_random_numbers(0, 127, 4)
    range1 = (range1_a, range1_b)
    range2 = (range2_a, range2_b)
    print('Range 1: ', range1)
    print('Range 2: ', range2)

    # Create a rhythm and duration from 0.1 to 1
    rhythm, duration = tuple([x / 10 for x in fetch_random_numbers(1, 10, 2)])
    print('Rhythm: ', rhythm)
    print('Duration: ', duration)

    # tell the score to use our composer to create the composition.
    composer1 = playstring(score, quote, rhythm,
                           duration, .9, chan=1, range=range1)
    composer2 = playstring(score, quote, rhythm,
                           duration, .9, chan=0, range=range2)
    score.compose([composer1, composer2])
    # write the midi file
    MidiFile("helloworld.mid", [meta, seq]).write()
    # success!
    print("Wrote helloworld.mid")


# TODO:
# upper case the string to move it to lower midi notes
# print the seq and/or midi file
# add a chan argument to helloworld and play drum map
# add metaseq with instruments
# add several composers
