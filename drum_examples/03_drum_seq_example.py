
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

# 6 tables de data pour gerer la sequence rythmique de chacun des sons.
# Si la valeur pour un temps de la mesure est 0, le son ne joue pas,
# si la valeur est positive, le son joue et la valeur controle son amplitude.
seqBass     = DataTable(16, init=[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
seqSnare    = DataTable(16, init=[0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0])
seqHiHat    = DataTable(16, init=[0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1])
seqCymbal   = DataTable(16, init=[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0])
seqCow      = DataTable(16, init=[(16-i)/32. for i in range(16)])
seqTamb     = DataTable(16, init=[i/16. for i in range(16)])

# Controles graphiques des sequences rythmiques.
seqBass.graph(title="Bass Drum")
seqSnare.graph(title="Snare")
seqHiHat.graph(title="Hi Hat")
seqCymbal.graph(title="Cymbal")
seqCow.graph(title="Cow Bell")
seqTamb.graph(title="Tambourine")

# Vitesse et compte des temps de la mesure.
metro       = Metro(15/baseBPM).play()
currentTap  = Counter(metro, min=0, max=16)

# On recupere l'amplitude pour le temps courant.
ampBass     = TableIndex(seqBass, currentTap)
ampSnare    = TableIndex(seqSnare, currentTap)
ampHiHat    = TableIndex(seqHiHat, currentTap)
ampCymbal   = TableIndex(seqCymbal, currentTap)
ampCow      = TableIndex(seqCow, currentTap)
ampTamb     = TableIndex(seqTamb, currentTap)

# Ceil retourne le plus petit entier plus grand ou egal a sa valeur en entree.
# Toute valeur plus grande que 0 retourne donc 1, c'est-a-dire un trig.
trigBass    = Ceil(ampBass, mul=metro)
trigSnare   = Ceil(ampSnare, mul=metro)
trigHiHat   = Ceil(ampHiHat, mul=metro)
trigCymbal  = Ceil(ampCymbal, mul=metro)
trigCow     = Ceil(ampCow, mul=metro)
trigTamb    = Ceil(ampTamb, mul=metro)

# Lecture des tables sur reception des trigs avec la valeur reelle du graph comme amplitude.
sigBass     = TrigEnv(trigBass, tableBass, dur=tableBass.getDur(), mul=ampBass)
sigSnare    = TrigEnv(trigSnare, tableSnare, dur=tableSnare.getDur(), mul=ampSnare)
sigHiHat    = TrigEnv(trigHiHat, tableHiHat, dur=tableHiHat.getDur(), mul=ampHiHat)
sigCymbal   = TrigEnv(trigCymbal, tableCymbal, dur=tableCymbal.getDur(), mul=ampCymbal)
sigCow      = TrigEnv(trigCow, tableCow, dur=tableCow.getDur(), mul=ampCow)
sigTamb     = TrigEnv(trigTamb, tableTamb, dur=tableTamb.getDur(), mul=ampTamb)

# On place chacun des sons dans l'espace stereo.
panBass     = Pan(sigBass, outs=2, pan=0.5)
panSnare    = Pan(sigSnare, outs=2, pan=0.25)
panHiHat    = Pan(sigHiHat, outs=2, pan=0.75)
panCymbal   = Pan(sigCymbal, outs=2, pan=0.35)
panCow      = Pan(sigCow, outs=2, pan=0.1)
panTamb     = Pan(sigTamb, outs=2, pan=0.9)

# Reverberation sur la somme des signaux stereo.
sum         = panBass + panSnare + panHiHat + panCymbal + panCow + panTamb
reverb      = STRev(sum, inpos=[0, 1], revtime=1, cutoff=5000, bal=0.1, mul=0.5).out()

s.gui(locals())
