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
rand = Randi(min=300.00, max=3000.00, freq=120.00, mul=1, add=0)
posi = 0

def function():
    global posi
    global sound
    global rand
    # longueur du son en sec
    info = sndinfo(sound)
    # valeur random entre 0 et longueur du son
    posi = random.uniform(0, info[1])
    newPos = posi + 0.03
    #if(posi > newPos):
    
    if (posi < 0.0 or posi > info[1]):
        print("info[1]", info[1])
        print("posi", posi)
        print("allo")
        posi = info[1]/2
    


pat = Pattern(function, time = .50).play()

amp = Fader(fadein=0.05, fadeout=0.36, dur=.35, mul=1, add=0)
player = SfPlayer(sound, speed=1, offset=posi, mul=amp).mix(2).out()
filter = Biquad(player, freq=rand, q=5, type=2, mul=1, add=0)
verb = Freeverb(filter, size=0.50, damp=0.50, bal=0.50, mul=1, add=0)
amp.play()
    
    



 




s.gui(locals())
