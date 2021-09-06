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


# define a composer (generator) that will add notes to our score.
def playstring(score: Score, string: str, rhy: float, dur: float, amp: float, chan: int = 0):
    # the builtin ord() function converts a single char into its
    # ascii code point (an integer 0-127). The builtin map() function
    # returns an iterator that will apply its first arg (a function)
    # to every element in its second arg (an iterable).
    for char in map(ord, string):
        # create a note to play each asci code point as a MIDI key number
        # with a specified onset, duration and amplitude.
        p = rescale(char, 0, 127, 34, 80)
        note = Note(time=score.now, duration=dur, pitch=p,
                    amplitude=amp, instrument=chan)
        # add the note at the current time in the score
        score.add(note)
        # yield back the time to wait until the composer is called again.
        yield rhy


if __name__ == '__main__':
    # allocate a sequence to hold our notes
    seq = Seq()
    meta = MidiFile.metatrack(ins={0: gm.BlownBottle})
    # allocate a score and give it the sequence
    score = Score(out=seq)
    # our text to play
    text = "Hello World!" * 4
    reverse_text = text[::-1]
    # tell the score to use our composer to create the composition.
    score.compose([playstring(score, text, 0.25, .25, .9, chan=9),
                  playstring(score, reverse_text, 0.25, .25, .9, chan=0)])
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
