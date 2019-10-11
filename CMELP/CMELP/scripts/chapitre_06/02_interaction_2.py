from pyo import *
import random
s = Server().boot()

# lecture d'un fichier son
snd = SfPlayer(SNDS_PATH + "/accord.aif", speed=[.998,1.003], 
               loop=True, mul=.35).stop()
# synthese FM
fm = FM(carrier=[99,99.7,100,100.4,100.9], ratio=.4987, index=8, mul=.1).stop()
# synthese additive
adsyn = SineLoop(freq=[random.uniform(145,155) for i in range(20)], 
                 feedback=.15, mul=.05).stop()

# src -> {'snd', 'fm', 'adsyn'}
def play(src="snd"):
    if src == 'snd':
        snd.out()
        fm.stop()
        adsyn.stop()
    elif src == 'fm':
        snd.stop()
        fm.out()
        adsyn.stop()
    elif src == 'adsyn':
        snd.stop()
        fm.stop()
        adsyn.out()

s.gui(locals())

