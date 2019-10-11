from pyo import *

s = Server().boot()

env = LinTable([(0,0), (300,1), (1000,.5), (3000,.5), (8191,0)], size=8192)

met = Beat(time=.25, taps=16, w1=50, w2=70, w3=50).play()
amp = TrigEnv(met, table=env, dur=met['dur'], mul=met['amp'])
fr = TrigXnoiseMidi(met, dist=12, x1=1, x2=.3, scale=0, mrange=(48,73))
frsnap = Snap(fr, choice=[0,2,3,5,7,8,11], scale=1)
osc = SineLoop(freq=frsnap, feedback=.08, mul=amp*.5).out()

met2 = Beat(time=.25, taps=16, w1=100, w2=40, w3=0).play()
amp2 = TrigEnv(met2, table=env, dur=met2['dur'], mul=met2['amp'])
fr2 = TrigXnoiseMidi(met2, dist=12, x1=1, x2=.3, scale=0, mrange=(36,61))
frsnap2 = Snap(fr2, choice=[0,2,3,5,7,8,11], scale=1)
osc2 = SineLoop(freq=frsnap2, feedback=.08, mul=amp2*.5).out(1)

s.gui(locals())