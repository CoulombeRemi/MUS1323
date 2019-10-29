from pyo import *
from random import choice

s = Server().boot()
s.amp = .5


## Melodie aleatoire
midi_Hz = [midiToHz(m) for m in [36,43,48,55,60,62,64,65,67,69,71,72]]
def meloRan():
    fm.carrier = choice(midi_Hz)
    fm_amp.play()
    i = 0
    #while (i != 3):
     #   if(i == 0):
      #      i+=1
       # if(i==3):
        #    i = 0 
        
pat = Pattern(meloRan, time = .125).play()



## Instrument de synthèse
fm_amp = Fader(dur=.1)
lfo = LFO(freq=60, sharp=0.50, type=0, mul=1, add=0)
fm = FM(ratio = lfo, mul = fm_amp)

delay = Delay(fm, delay=1, feedback=0, mul=1)
verb = Freeverb(delay, size=[.79,.8], damp=.9, bal=.3).out()


x = Spectrum(verb)
s.gui(locals())
