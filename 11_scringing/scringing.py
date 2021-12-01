import math
from musx.gens import markov_analyze
from musx.ran import between
import pythonosc.udp_client
import threading, time
import musx

LOCRIAN = 'a4 g f Eb d c Bb3 a3'
PHRYGIAN = 'a4 g f e d c Bb3 a3'
AEOLIAN = 'a4 g f e d c b3 a3'
DORIAN = 'a4 g f# e d c b3 a3'
MIXOLYDIAN = 'a4 g f# e d c# b3 a3'
IONIAN = 'a4 g# f# e d c# b3 a3'
LYDIAN = 'a4 g# f# e d# c# b3 a3'

MODES = [
    LOCRIAN, PHRYGIAN, AEOLIAN, DORIAN, MIXOLYDIAN, IONIAN, LYDIAN
]

# Support for sending OSC messages in realtime.

class OscMessage(musx.Event):
    """
    A class to represent OSC messages.
    
    Parameters
    ----------
    addr : string
        An OSC address (a string identifier starting with '/', for example "/musx").
    time : float | int
        The start time of the event.
    *data : variadic args
        A sequence of zero or more values that constitute the message's data.
    """
    def __init__(self, addr, time, *data):
        super().__init__(time)
        self.addr = addr
        self.data = [time, *data]
    def __str__(self):
        return f"<OscMessage: '{self.addr}' {self.data} {hex(id(self))}>"
    __repr__ = __str__


def oscplayer(oscseq, oscout):
    """
    Send OSC messages in real time from a thread.
    
    Parameters
    ----------
    oscseq : Seq
        A Seq containing a time sorted list of OscMessages.
    oscport : pythonosc.udp_client.SimpleUDPClient
        An open OSC output port.
    """
    messages = oscseq.events
    length = len(messages)
    thistime = messages[0].time
    nexttime = thistime
    i = 0
    while i < length:
        if messages[i].time == thistime:
            #print(f'playing {messages[i]}')
            oscout.send_message(messages[i].addr, messages[i].data)
            i += 1
            continue
        # if here then midi[i] is later than thistime so sleep
        nexttime = messages[i].time
        #print(f'waiting {nexttime-thistime}')
        time.sleep(nexttime - thistime) 
        thistime = nexttime

def generate_pattern(original_pattern: list, order: int = between(1, 4)):
    rules = markov_analyze(original_pattern, order)
    gen = musx.markov(rules)
    return [next(gen) for _ in range(len(original_pattern))]

def plain_hunt(score: musx.Score, rhy: float, dur: float):
    """
    A composer function that generates osc messages using the
    Plain Hunt change ringing pattern. See also: `cring.py`.
    """
    # one octave of bells numbered 8, 7, ... 1
    bells = [n for n in range(8, 0, -1)]
    
    # Plain Hunt's rotation rules
    rules = [[0, 2, 1], [1, 2, 1]]
    # generate the Plain Hunt pattern for 8 bells
    peals = musx.all_rotations(bells, rules, True, True)
    
    # write OscMessages to the OscSeq
    num_groups = len(peals)
    num_sections = math.floor(num_groups / len(MODES))
    for i, group in enumerate(peals):
        for b in group:
            mode_idx = math.floor(musx.rescale(i, 0, num_groups, 0, len(MODES)))
            mode = MODES[mode_idx]
            # dictionary of frequencies each bell plays (D major)
            freqs = {i:f for i,f in zip(bells, musx.hertz(mode))}
            f = freqs[b]
            m = OscMessage("/musx", score.now, dur, f, .3)
            score.add(m)
            yield rhy

## Add your code here!

        
if __name__ == '__main__':
    print('Hiho!')
    oscout = pythonosc.udp_client.SimpleUDPClient("127.0.0.1", 57120)
    oscseq = musx.Seq()   
    score = musx.Score(out=oscseq)
    score.compose(plain_hunt(score, .3, 1.5))
    player = threading.Thread(target=oscplayer, args=(oscseq, oscout))
    player.start()
    print('OK!')
