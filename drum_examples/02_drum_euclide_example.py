
from pyo import *

s = Server().boot()

baseBPM     = Sig(90)
baseBPM.ctrl([SLMap(30, 208, "lin", "value", 90)], title="Tempo BPM")

tableBass   = SndTable('bd.aif')
tableSnare  = SndTable('snare.aif')
tableHiHat  = SndTable('hh.aif')
tableCymbal = SndTable('cymbal.aif')
tableCow    = SndTable('cow.aif')
tableTamb   = SndTable('tamb.aif')

trigs       = Euclide(time=15/baseBPM, taps=32, onsets = [4,9, 8, 3, 11, 10]).play()
trigs.ctrl()

sigBass     = TrigEnv(trigs[0], tableBass, dur=tableBass.getDur(), mul=trigs["amp"][0])
sigSnare    = TrigEnv(trigs[1], tableSnare, dur=tableSnare.getDur(), mul=trigs["amp"][1])
sigHiHat    = TrigEnv(trigs[2], tableHiHat, dur=tableHiHat.getDur(), mul=trigs["amp"][2])
sigCymbal   = TrigEnv(trigs[3], tableCymbal, dur=tableCymbal.getDur(), mul=trigs["amp"][3])
sigCow      = TrigEnv(trigs[4], tableCow, dur=tableCow.getDur(), mul=trigs["amp"][4])
sigTamb     = TrigEnv(trigs[5], tableTamb, dur=tableTamb.getDur(), mul=trigs["amp"][5])

panBass     = Pan(sigBass, outs=2, pan=0.5)
panSnare    = Pan(sigSnare, outs=2, pan=0.25)
panHiHat    = Pan(sigHiHat, outs=2, pan=0.75)
panCymbal   = Pan(sigCymbal, outs=2, pan=0.35)
panCow      = Pan(sigCow, outs=2, pan=0.1)
panTamb     = Pan(sigTamb, outs=2, pan=0.9)

sum         = panBass + panSnare + panHiHat + panCymbal + panCow + panTamb
reverb      = STRev(sum, inpos=[0, 1], revtime=1, cutoff=5000, bal=0.1, mul=0.5).out()

s.gui(locals())
