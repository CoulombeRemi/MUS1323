from pyo import *
import random

s = Server().boot()

snd_amp = Fader(fadein=5, fadeout=5, dur=0)
snd = SfPlayer(SNDS_PATH + "/accord.aif", speed=[.998,1.003], 
               loop=True, mul=snd_amp*.35).out()
fm_amp = Fader(fadein=5, fadeout=5, dur=0)
fm = FM(carrier=[99,99.7,100,100.4,100.9], ratio=.4987, 
                index=8, mul=fm_amp*.1).out()
adsyn_amp = Fader(fadein=5, fadeout=5, dur=0)
adsyn = SineLoop(freq=[random.uniform(145,155) for i in range(20)], 
                 feedback=.15, mul=adsyn_amp*.05).out()

def play_snd(state=1):
    if state == 1:
        snd.speed = [random.choice([.5,.67,.75,1,1.25,1.5]) for i in range(2)]
        snd_amp.play()
    else:
        snd_amp.stop()

def play_fm(state=1):
    if state == 1:
        freq = random.randint(0,7)*25+50
        fm.carrier = [freq*random.uniform(.99,1.01) for i in range(5)]
        fm_amp.play()
    else:
        fm_amp.stop()

def play_adsyn(state=1):
    if state == 1:
        freq = random.randint(0,7)*25+50
        adsyn.freq = [freq*random.uniform(.99,1.01) for i in range(20)]
        adsyn_amp.play()
    else:
        adsyn_amp.stop()

def event_0():
    play_fm()
def event_1():
    pass
def event_2():
    play_snd()
def event_3():
    play_adsyn()
    play_fm(0)
def event_4():
    pass
def event_5():
    play_snd(0)
    play_fm()
def event_6():
    play_adsyn(0)
def event_7():
    play_snd()
def event_8():
    play_fm(0)
    play_adsyn()
def event_9():
    pass
def event_10():
    play_snd(0)
    play_adsyn(0)
    met.stop()

met = Metro(time=5).play()
count = Counter(met, min=0, max=11)
score = Score(count, fname="event_")

s.gui(locals())
