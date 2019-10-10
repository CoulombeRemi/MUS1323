from pyo import *

s = Server().boot()

lfg = Sine(350, 0)
lfd = Sine(350, 0.5)


s.gui(locals())