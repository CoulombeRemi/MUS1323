from pyo import *

s = Server().boot()

env = HannTable()
table = SndTable("Beethoven.aif")
table.view()

# exemple 0 -> changement de vitesse sans toucher a la hauteur
# exemple 1 -> position de lecture aleatoire
ex = 0
if ex == 0:
    pos = Phasor(freq=table.getRate() * 0.25, mul=table.getSize())
elif ex == 1:
    pos = Randi(min=0, max=table.getSize(), freq=2)

pit = [1., 1.002]
dur = Noise(mul=.002, add=.1)   # legeres variations de la duree des grains

grain = Granulator( table=table,    # table contenant les echantillons
                    env=env,        # enveloppe des grains
                    pitch=pit,      # pitch global des grains
                    pos=pos,        # position de lecture, en echantillons
                    dur=dur,        # duree des grains en secondes
                    grains=32,      # nombre de grains
                    basedur=.1,     # duree de reference pour les grains 
                                    # (si dur == basedur, pas de transpo)
                    mul=.1).out()

s.gui(locals())
