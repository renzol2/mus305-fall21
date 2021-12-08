import musx
import pythonosc.udp_client
import scosc  # in this script's directory
from phrases import Phrase, DUYUG_CR_1_SAMPLE, DUYUG_A_BINALIG_C4_14_SAMPLE

OSC_ADDRESS = '/musx/kulintang'


def playvkey(score: musx.Score, scale: list[int], rules: list, rhy: float, dur: float, amp: float):
    for gong in musx.all_rotations(scale, rules, False, True):
        now = 0
        # OSC MSG:   "pattern", scoretime, args...
        # VKEY ARGS: keynum, start=0, dur=nil, amp=1, pan=0, out=0, ampenv=nil, bend=nil
        msg = scosc.OscMessage(
            OSC_ADDRESS, score.now+now, gong, 0, dur, amp)
        score.add(msg)
        now += rhy
        yield now


def plain_hunt():
    return [[0, 2, 1], [1, 2, 1]]


def compose_phrase(score: musx.Score, phrase: Phrase, dur: float, amp: float, tempo: int):
    '''
    Adds a single kulintang phrase to the given score
    '''
    for gong_num, beat_length, accent in phrase:
        now = 0

        # Add notes to score, depending on if there are 1-2 notes at the same time
        if isinstance(gong_num, int):
            msg = scosc.OscMessage(
                OSC_ADDRESS, score.now + now, gong_num, 0, dur, amp)
            score.add(msg)
        else:
            # In this case, gong_num is a 2-tuple
            msgs = [
                scosc.OscMessage(
                    OSC_ADDRESS, score.now + now, num, 0, dur, amp
                ) for num in gong_num
            ]
            for msg in msgs:
                score.add(msg)
        
        now += musx.intempo(beat_length, tempo)
        yield now


if __name__ == '__main__':
    print(DUYUG_CR_1_SAMPLE)
    oscout = pythonosc.udp_client.SimpleUDPClient("127.0.0.1", 57120)
    print(oscout)

    scale = [i for i in range(8)]

    dur = 0.5
    amp = 0.5
    tempo = 100

    seq = musx.Seq()
    score = musx.Score(out=seq)
    score.compose(compose_phrase(score, DUYUG_CR_1_SAMPLE + DUYUG_A_BINALIG_C4_14_SAMPLE, dur, amp, tempo))
    scosc.oscplayer(seq, oscout)
