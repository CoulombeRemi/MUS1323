from pyo import *
import random

s = Server().boot()

fr = Randi(min=295, max=300, freq=[random.uniform(2,8) for i in range(100)])
sines = SineLoop(fr, feedback=.08, mul=.01).out()
print(len(sines))

s.gui(locals())
