from pyo import *
from random import choice

s = Server().boot()
s.amp = .35


## Melodie aleatoire
midi_Hz = [midiToHz(m) for m in [36,43,48,55,60,62,64,65,67,69,71,72]]
print(midi_Hz)
trig = 0
accent = [1,0,0,0]

def meloRan():
    global trig
    fm.carrier = choice(midi_Hz)
    if accent[trig] == 1:
        fm.mul = fm_amp*1.25
        print("+")
    else : 
        fm.mul = fm_amp*1
        print("-")
    fm_amp.play()
    trig += 1
    if trig == len(accent):
        trig = 0

        
pat = Pattern(meloRan, time = .125).play()



## Instrument de synthèse
fm_amp = Fader(dur=.1)
lfo = LFO(freq=60, sharp=0.50, type=0, mul=1, add=0)
fm = FM(ratio = lfo, mul = fm_amp).mix(2)
delay = Delay(fm, delay=1, feedback=0, mul=1)
verb = Freeverb([fm, delay], size=[.79,.8], damp=.9, bal=.3).out()


x = Spectrum(verb)
s.gui(locals())
