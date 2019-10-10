#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from malibrairie import Particule
import random

s = Server().boot()

### Differentes sources sonores ###
a = Noise(.3)
a1 = SineLoop(freq=50, feedback=.2, mul=1)
a2 = FM(carrier=100, ratio=5.67, index=20, mul=.3)

### 5 exemples d'utilisation de la classe Particule ###
which = 0
if which == 0:
    b = Particule(a, time=.125, q=2, maxdur=.5).out()
elif which == 1:
    qlfo = Sine(.1, mul=5, add=6)
    b = Particule(a, time=.125, q=qlfo, maxdur=.25).out() 
elif which == 2:
    tlfo = Sine(.15, mul=.1, add=.15)
    qlfo = Sine(.1, mul=5, add=6)
    b = Particule(a, time=tlfo, q=qlfo, maxdur=.25).out()
elif which == 3:
    b = Particule(input=a, time=.25, q=10, maxdur=.5, frange=[350,1000]).out()
    c = Particule(a, time=.125, q=5, maxdur=.25, frange=[2000,10000]).out()
elif which == 4:
    tlfo = Sine(.15, mul=.1, add=.15)
    qlfo = Sine(.1, mul=5, add=6)
    b = Particule(a, time=tlfo, q=qlfo, maxdur=.25)
    d = Delay(b.getOut().mix(2), delay=.5, feedback=.75)
    c = Freeverb(d, size=.8, damp=.9, bal=.4).out()

def change():
    y = random.randint(0,2)
    if y == 0:
        b.setInput(a, 2)
    elif y == 1:
        b.setInput(a1, 2)
    elif y == 2:
        b.setInput(a2, 2)

# "pat.play()" active le changement de source automatique
pat = Pattern(change, 5)

s.gui(locals())
