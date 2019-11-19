
from pyo import *

s = Server().boot()

# Controle de la vitesse en BPM.
baseBPM     = Sig(90)
baseBPM.ctrl([SLMap(30, 208, "lin", "value", 90)], title="Tempo BPM")

# On charge le ssons dans les tables.
tableBass   = SndTable('bd.aif')
tableSnare  = SndTable('snare.aif')
tableHiHat  = SndTable('hh.aif')
tableCymbal = SndTable('cymbal.aif')
tableCow    = SndTable('cow.aif')
tableTamb   = SndTable('tamb.aif')

# Poids pour les temps forts, intermediaires et faibles a l'initialisation.
weightBass  = [100, 40, 20]
weightSnare = [50, 90, 20]
weightHiHat = [20, 70, 70]
weightCymbal= [50, 20, 0]
weightCow   = [40, 40, 40]
weightTamb  = [0, 80, 20]
# Liste de listes de poids pour simplifier la mise en place dans l'objet Beat.
weightAll   = [weightBass, weightSnare, weightHiHat, weightCymbal, weightCow, weightTamb]

# Gestion du rythme.
# 15/baseBPM donne la duree de la double-croche (60/BPM est la duree de la noire).
# On construit les listes de poids en reunissant la valeur a la position 0, 1 ou 2 de toutes
# les sous-listes dans la liste weightAll. 6 objects Beat seront donc crees a l'interne.  
trigs       = Beat(time=15/baseBPM, taps=16,
                   w1 = [w[0] for w in weightAll],
                   w2 = [w[1] for w in weightAll],
                   w3 = [w[2] for w in weightAll]).play()
trigs.ctrl()

# Lecture des tables sur reception des trigs. On recupere les objets Beat individuels avec
# la notation utilisee pour la pige dans une liste, en donnant la position entre crochets. 
sigBass     = TrigEnv(trigs[0], tableBass, dur=tableBass.getDur(), mul=trigs["amp"][0])
sigSnare    = TrigEnv(trigs[1], tableSnare, dur=tableSnare.getDur(), mul=trigs["amp"][1])
sigHiHat    = TrigEnv(trigs[2], tableHiHat, dur=tableHiHat.getDur(), mul=trigs["amp"][2])
sigCymbal   = TrigEnv(trigs[3], tableCymbal, dur=tableCymbal.getDur(), mul=trigs["amp"][3])
sigCow      = TrigEnv(trigs[4], tableCow, dur=tableCow.getDur(), mul=trigs["amp"][4])
sigTamb     = TrigEnv(trigs[5], tableTamb, dur=tableTamb.getDur(), mul=trigs["amp"][5])

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

# On genere une nouvelle rythmique aux quatre mesures.
barCount = 0
def endOfBar():
    global barCount
    if barCount % 4 == 0:
        trigs.new()        
    barCount += 1

# Appelle la fonction endOfBar() a la fin de la mesure.
tf = TrigFunc(trigs["end"][0], function=endOfBar)

s.gui(locals())
