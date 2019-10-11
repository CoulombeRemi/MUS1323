from pyo import *
import random

s = Server().boot()

amp = Fader(fadein=0.25, fadeout=0.25, dur=0, mul=0.3).play()
noz = Noise(mul=amp)
fbank = ButBP(noz, freq=[250,700,1800,3000], q=40, mul=4).out()

def change():
    f1 = random.uniform(200,500)
    f2 = random.uniform(500,1000)
    f3 = random.uniform(1000,2000)
    f4 = random.uniform(2000,4000)
    fbank.freq = [f1, f2, f3, f4]

lfo = Sine(.1, mul=.5, add=.75)
pat = Pattern(function=change, time=lfo).play()

s.gui(locals())

