from pyo import *
import random
s = Server().boot()

#fr = Randi(min=295, max=300, freq=[random.uniform(2, 8) for i in range(10)])
amp = Randi(min=0, max=0.5, freq=[random.uniform(0.25, 1) for i in range(10)])
#sines = SineLoop(freq=fr, feedback=0.03, mul=amp).out()
sines = SineLoop(freq=[i*100+50 for i in range(10)], feedback=0.03, mul=amp).out()

s.gui(locals())