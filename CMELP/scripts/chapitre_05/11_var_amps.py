from pyo import *
import random

s = Server().boot()

amp = Randi(min=0, max=.05, freq=[random.uniform(.25,1) for i in range(10)])
sines = SineLoop(freq=[i*100+50 for i in range(10)], feedback=.03, mul=amp).out()

s.gui(locals())