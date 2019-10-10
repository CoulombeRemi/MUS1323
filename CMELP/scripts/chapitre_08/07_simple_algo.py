from pyo import *

s = Server().boot()

env = LinTable([(0,0), (300,1), (1000,.5), (3000,.5), (8191,0)], size=8192)

met = Beat(time=.125, taps=16, w1=90, w2=50, w3=30).play()

amp = TrigEnv(met, table=env, dur=met['dur'], mul=met['amp'])

fr = TrigXnoiseMidi(met, dist=12, x1=1, x2=.3, scale=0, mrange=(48,85))
frsnap = Snap(fr, choice=[0,2,3,5,7,8,11], scale=1)

osc = SineLoop(freq=frsnap, feedback=.08, mul=amp*.5).out()

s.gui(locals())