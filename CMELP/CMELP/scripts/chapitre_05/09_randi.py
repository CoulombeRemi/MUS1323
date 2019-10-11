from pyo import *
s = Server().boot()

rnd = Randi(min=390, max=410, freq=4)
a = Sine(freq=rnd, mul=.5).out()

s.gui(locals())
