from pyo import *

s = Server().boot()

env = LinTable([(0,0), (100,1), (500,.5), (5000,.5), (8191,0)], size=8192)
globenv = HannTable()

notes = [midiToHz(x) for x in [60,62,64,65,67,69,71,72]]

globmet = Metro(time=5).play()
globamp = TrigEnv(globmet, table=globenv, dur=5)

met = Metro(time=.125, poly=2).play()
t = TrigChoice(met, choice=notes, port=0.005)
amp = TrigEnv(met, table=env, dur=.25, mul=.5)
a = SineLoop(freq=t, feedback=0.07, mul=amp*globamp).out()

s.gui(locals())