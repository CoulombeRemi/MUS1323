from pyo import *
import random

s = Server().boot()

#########################################################################
### SNDS_PATH est un string provenant du module pyo qui pointe sur le ###
### dossier ou sont installes les sons fournis avec pyo. N'utilisez   ###
### jamais cette constante pour lire vos propre sons.                 ###
#########################################################################
son = SNDS_PATH + "/transparent.aif"

# Garde en memoire la duree du son (2e element de la liste que retourne sndinfo).
son_dur = sndinfo(son)[1]
print("Duree du son :", son_dur)

# Liste de notes midi pour restreindre les transposition permises.
mnotes = [48, 50, 53, 55, 57, 60, 62, 65, 67, 69, 72]
# Conversion en facteur de transposition autour de la note 60.
transpos = [midiToTranspo(x) for x in mnotes]

####### Processus audio  #######

# Enveloppe et mise en place d'un lecteur de son.
f = Fader(fadein=.005, fadeout=.01, dur=.02)
sf = SfPlayer(son, speed=1, mul=f)

# Banque de delais (4 delais avec feedback differents).
dls = Delay(sf, delay=[.1,.2,.3,.4], feedback=[.25,.5,.35,.75], 
            maxdelay=1, mul=.25)
# Disposition dans l'espace stereo de chacun des delais.
pan = Pan(dls, pan=[0,.33,1,.66], spread=.25)
# Reverbe generale, mix(2) pour une reverbe stereo.
rev = WGVerb(pan.mix(2), feedback=.8, cutoff=4000, bal=.15).out()

####### Section controle  #######

# Gestion des methodes de controle. Voir la fonction "new_stream" pour
# la signification de ces variables. Valeurs possibles, 0 ou 1.
offset_meth = 0
speed_meth = 0

# Position du grain dans le son en secondes (pour la methode 1 a offset_meth).
start = 0

# Increment sur la position en seconde. Appliquee a chaque appel de new_stream.
start_inc = 0.01

# Fonction appelee periodiquement par l'objet Pattern (plus bas).
def new_stream():
    # variable globale puisque qu'on veut la modifier.
    global start

    # si offset_meth vaut 0, on pige un point de lecture au hasard.
    # Sinon, on avance dans le son en fonction de l'increment. On ne 
    # declare pas l'increment global puisqu'on ne le modifie pas!
    if offset_meth == 0:
        sf.offset = random.uniform(0, son_dur-.1)
    else:
        start += start_inc
        if start >= (son_dur-.1): # Rendu a la fin du son, on revient au debut.
            start = 0
        sf.offset = start

    # si speed_meth vaut 0, on pige une transposition dans la liste de transpos.
    # Sinon, on pige une legere deviation autour de 1.
    if speed_meth == 0:
        sf.speed = random.choice(transpos)
    else:
        sf.speed = random.uniform(.99, 1.01)

    # Nouvelle duree de grain.
    f.dur = random.uniform(.02, .1)

    # Affichage des nouvelles valeurs.
    print("offset: %.2f, speed: %.2f, dur: %.2f" % (sf.offset, sf.speed, f.dur))

    # On lance la lecture du son et de l'enveloppe d'amplitude.
    sf.play()
    f.play()

# Variations sur la frequence des appels de la fonction new_stream.
vtime = Choice(choice=[.2, .4, .8, 1.2, 2.4], freq=1./2.4)

# Pattern appelle de facon periodique la fonction donnee en argument 
# (new_stream *sans parentheses*). On *doit* appeler la methode play()
# de l'objet Pattern pour l'activer.
pat = Pattern(time=vtime, function=new_stream).play()

s.gui(locals())
