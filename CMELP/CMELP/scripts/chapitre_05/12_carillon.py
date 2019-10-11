from pyo import *

s = Server().boot()

pits = [midiToHz(m) for m in [36,43,48,55,60,62,64,65,67,69,71,72]]
choix = Choice(choice=pits, freq=[1,2,3,4])
sines = SineLoop(freq=choix, feedback=.05, mul=.1).out()

s.gui(locals())
