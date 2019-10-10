from pyo import *

s = Server().boot()

pits = [midiToHz(m) for m in [36,43,48,55,60,62,64,65,67,69,71,72]]

choix = Choice(choice=pits, freq=[1,2,3,4])
ch_port = Port(choix, risetime=.001, falltime=.001)

lffeed = Sine(freq=0.1, mul=.07, add=.07)
sines = SineLoop(freq=ch_port, feedback=lffeed, mul=.1)

lfind = Sine(freq=0.1, phase=0.5, mul=3, add=3)
fms = FM(carrier=ch_port, ratio=1.0025, index=lfind, mul=.025)

src_sum = sines.mix(2) + fms.mix(2)

lfdel = Sine(.1, mul=.003, add=.005)
comb = Delay(src_sum, delay=lfdel, feedback=.5)

# Sommation des sources et du delai
out_sum = src_sum + comb
# Envoie vers le reverbe et sortie du signal
rev = WGVerb(out_sum, feedback=.8, cutoff=3500, bal=.4).out()

s.gui(locals())

