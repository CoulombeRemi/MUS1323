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
dur = sndinfo(sound)[1]

f = Fader(fadein=0.005, fadeout=0.005, dur=0.035)
sf = SfPlayer(sound, speed=1, mul=f)
lfo = Sine([.1, .15]).range(300, 3000)
filt = ButBP(sf, freq=lfo, q=2)
rev = WGVerb(filt, feedback=0.9, bal=0.25).out()

start = dur * 0.5
def choose():
    global start
    sf.offset = start
    sf.play()
    f.play()
    start += random.uniform(-0.03, 0.03)
    if start < 0.0 or start > dur:
        start = dur * 0.5
    
pat = Pattern(choose, 0.05).play()

s.gui(locals())
