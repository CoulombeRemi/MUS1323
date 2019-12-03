from pyo import *


s = Server().boot()



sf = SfPlayer("drum.wav", speed=1, loop=True, mul=1)
sf.out()

print(sf.Velocity)












s.gui(locals())