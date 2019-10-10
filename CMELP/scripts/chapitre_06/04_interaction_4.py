from pyo import *
import random
s = Server().boot()

snd_amp = Fader(fadein=5, fadeout=5, dur=0)
snd = SfPlayer(SNDS_PATH + "/accord.aif", speed=[.998,1.003], 
               loop=True, mul=snd_amp*.35).out()
fm_amp = Fader(fadein=5, fadeout=5, dur=0)
fm = FM(carrier=[80,79.7,81,81.4,81.9], ratio=.4987, index=8, mul=fm_amp*.1).out()
adsyn_amp = Fader(fadein=5, fadeout=5, dur=0)
adsyn = SineLoop(freq=[random.uniform(145,155) for i in range(20)], 
                 feedback=.15, mul=adsyn_amp*.05).out()

last = None
def play():
    global last
    src = random.choice(['snd', 'fm', 'adsyn'])
    while src == last:
        print('"%s" is already playing, choosing another...' % src)
        src = random.choice(['snd', 'fm', 'adsyn'])
    last = src
    print(src)
    if src == 'snd':
        snd_amp.play()
        fm_amp.stop()
        adsyn_amp.stop()
    elif src == 'fm':
        snd_amp.stop()
        fm_amp.play()
        adsyn_amp.stop()
    elif src == 'adsyn':
        snd_amp.stop()
        fm_amp.stop()
        adsyn_amp.play()


pat = Pattern(function=play, time=6).play()

s.gui(locals())

