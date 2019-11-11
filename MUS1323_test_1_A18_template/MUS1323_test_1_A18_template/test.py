"""
MUS 1323 - A18 - test 1 - Space Invaders
========================================

À l'aide du fichier sonore fourni et référencé dans la variable "sound",
vous devez construire un programme qui génère une multitude de petits 
grains de sons filtrés et réverbérés.

Instrument
----------
1 - Une enveloppe d'amplitude, d'une durée totale de 35 millisecondes,
    doit être appliquée à une lecture du fichier son 'mus1323_test_1.wav'.
2 - La lecture du son doit passer dans deux filtres passe-bande dont les 
    fréquences oscillent lentement entre 300 et 3000 Hz. La vitesse 
    d'oscillation doit être différente pour chacun des deux filtres.
3 - Les signaux en sortie des filtres doivent être donnés en entrée d'une
    réverbération. Utilisez la réverbération pour contrôler le rapport
    entre le signal direct et le signal réverbéré.
    
Fonction de contrôle
--------------------
1 - Vous devez créer une fonction qui sera exécutée à toutes les 50
    millisecondes. Elle doit activer la lecture d'un grain et son enveloppe.
2 - À chaque exécution, la fonction doit assigner un nouveau point de 
    départ au lecteur de fichier son. Le nouveau point de départ doit 
    être choisi au hasard mais ne peut être éloigné du point de départ 
    précédent de plus de 30 millisecondes, positif ou négatif.
3 - Si le point de départ choisi est plus petit que 0 ou plus grand que
    la durée du son, il doit être automatiquement fixé à la moitié de la
    durée du son, voir sndinfo() dans le manuel.

"""

from pyo import *
import random
s = Server().boot()
sound = 'mus1323_test_1.wav'
dure = sndinfo(sound)[1]
amp = Fader(fadein=0.05, fadeout=0.05, dur=0.035, mul=1, add=0)
snd = SfPlayer(sound, speed=1, mul=amp)
lfo = (Sine([.1, .15])).range(300, 3000)
filter = ButBP(snd, freq=lfo, q=2, mul=1, add=0)
verb = Freeverb(filter, size=0.50, damp=0.50, bal=0.25, mul=1, add=0).out()
start = dure*.5

def playMark():
    global start
    snd.offset = start
    snd.play()
    amp.play()
    start += random.uniform(-.03, .03)
    if (start < 0.0 or start > dure):
        start = dure/2

pat = Pattern(playMark, time=.05, arg=None).play()

lfoSpec = Spectrum(lfo, size=1024)
filterSpec = Spectrum(filter, size=1024)
s.gui(locals())
