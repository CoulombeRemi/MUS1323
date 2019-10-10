from pyo import *

s = Server().boot()

notes = [midiToHz(x) for x in [60,62,64,65,67,69,71,72]]
met = Metro(time=.125).play()
t = TrigChoice(met, choice=notes, port=0.005)
a = SineLoop(freq=t, feedback=0.07, mul=.3).out()

s.gui(locals())