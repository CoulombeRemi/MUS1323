"""
------------------------------ Le hacheur malade ------------------------------
1 - Dans un premier temps, récupérer la durée du son "solitaryLoop.wav" et
    conserver la dans une variable globale.
    
2 - Charger le son dans un SfPlayer dont l'amplitude est contrôlée par une
    enveloppe de type attaque-relâche (fadein-fadeout) pour éliminer les clics.
    
3 - Dans une fonction, vous devez choisir un point de départ dans le son, une
    vitesse de lecture (transposition) et une durée de jeu de façon aléatoire.
    *La lecture ne doit pas dépasser la durée du son.* Ces valeurs doivent
    être assignées à l'enveloppe et au SfPlayer. Ensuite la fonction fait
    jouer le son et son enveloppe.
    
4 - Les appels successifs de la fonction doivent être automatiques et doivent
    aussi respecter la durée pigée, c'est à dire que le prochain appel
    attend que la lecture en cours soit terminée.
    
5 - Le son haché doit ensuite passer dans une réverbération.

"""
### 13/15

from pyo import *
import random
s = Server().boot()
s.amp = 0.3

son = 'solitaryLoop.wav'
sndLength = sndinfo(son)[1] # 5.63 sec.
env = Fader(fadein=0.25, fadeout=0.25)
sf = SfPlayer(son, mul=env)
verb = Freeverb(sf, size=0.50, damp=0.50, bal=0.5, mul=1, add=0).out()


dure = 1
def choice():
    # choix length 
    global dure
    dure= random.uniform(0.1, sndLength)
    env.dur = dure

    ### Assigner la duree de jeu du segment a l'attribut "time" du Pattern.

    ### duree + offset depaase souvent la fin du son.
    
    # choix du point de départ
    sf.offset = random.uniform(0, sndLength)
    # choix du pitch
    sf.speed = random.random()+0.5
    
    print("speed function",sf.speed)
    print("start function", sf.offset)
    print("length function", env.dur)
    print("_______")
    sf.play()
    env.play()
    return dure

### dure vaut 1 lorsque cette ligne est executee.
pat = Pattern(choice, time=dure).play()
print("length ", dure)

s.gui(locals())