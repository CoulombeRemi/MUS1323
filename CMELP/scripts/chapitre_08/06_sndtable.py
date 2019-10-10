from pyo import *

s = Server().boot()

snd = SndTable(SNDS_PATH + "/accord.aif")
dur = snd.getDur()
print("Duree:", dur)

met = Metro(time=dur).play()
out = TrigEnv(met, table=snd, dur=dur).out()

s.gui(locals())