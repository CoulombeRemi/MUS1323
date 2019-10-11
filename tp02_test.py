from pyo import *
import random

s = Server(sr=44100, nchnls=2, buffersize=256, duplex=1).boot()
s.amp = .05

val = None
def midiRand():
    global val
    mon_pitch = [midiToHz(m) for m in [32,43,48,55,60,62,64,65,67,69,71,72]]
    val = random.choice(mon_pitch)
    fm.carrier=val
    fm_amp.play()
    return val
    
pat = Pattern(function=midiRand, time = .125)
pat.play()

fm_amp = Fader(dur=0.1)
lf1 = LFO(freq=100, sharp=0.50, type=0, mul=1, add=0)
fm = FM(carrier=100, ratio=lf1, index=5, mul=fm_amp, add=0)

dl1 = Delay(fm, delay=1, feedback=0, maxdelay=1, mul=1, add=0)
vrb = Freeverb(dl1, size=0.50, damp=0.50, bal=0.50, mul=1, add=0).mix(2).out()

s.gui(locals())