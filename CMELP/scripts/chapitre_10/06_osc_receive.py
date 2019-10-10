from pyo import *

s = Server().boot()

table = SndTable("Beethoven.aif")
env = HannTable()

# Ecoute le port 9000 aux destinations '/pos' et '/rand'
rec = OscReceive(port=9000, address=['/pos', '/rand'])

# rec['/pos'] -> position de lecture
# rec['/rand'] -> random pour la duree des grains
pos = Port(rec['/pos'], risetime=.05, falltime=.05, mul=table.getSize())

pit = [1., 1.002]

# legeres variations de la duree des grains
dur = Noise(mul=Clip(rec['/rand'], min=0, max=.09), add=.1)

grain = Granulator( table=table,    # table contenant les echantillons
                    env=env,        # enveloppe des grains
                    pitch=pit,      # pitch global des grains
                    pos=pos,        # position de lecture, en echantillons
                    dur=dur,        # duree des grains en secondes
                    grains=32,      # nombre de grains
                    basedur=.1,     # duree de reference pour les grains 
                    mul=.1).out()

s.gui(locals())