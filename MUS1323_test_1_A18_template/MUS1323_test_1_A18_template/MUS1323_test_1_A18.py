"""
MUS 1323 - A18 - test 1 - Space Invaders
========================================

� l'aide du fichier sonore fourni et r�f�renc� dans la variable "sound",
vous devez construire un programme qui g�n�re une multitude de petits 
grains de sons filtr�s et r�verb�r�s.

Instrument
----------
1 - Une enveloppe d'amplitude, d'une dur�e totale de 35 millisecondes,
    doit �tre appliqu�e � une lecture du fichier son 'mus1323_test_1.wav'.
2 - La lecture du son doit passer dans deux filtres passe-bande dont les 
    fr�quences oscillent lentement entre 300 et 3000 Hz. La vitesse 
    d'oscillation doit �tre diff�rente pour chacun des deux filtres.
3 - Les signaux en sortie des filtres doivent �tre donn�s en entr�e d'une
    r�verb�ration. Utilisez la r�verb�ration pour contr�ler le rapport
    entre le signal direct et le signal r�verb�r�.
    
Fonction de contr�le
--------------------
1 - Vous devez cr�er une fonction qui sera ex�cut�e � toutes les 50
    millisecondes. Elle doit activer la lecture d'un grain et son enveloppe.
2 - � chaque ex�cution, la fonction doit assigner un nouveau point de 
    d�part au lecteur de fichier son. Le nouveau point de d�part doit 
    �tre choisi au hasard mais ne peut �tre �loign� du point de d�part 
    pr�c�dent de plus de 30 millisecondes, positif ou n�gatif.
3 - Si le point de d�part choisi est plus petit que 0 ou plus grand que
    la dur�e du son, il doit �tre automatiquement fix� � la moiti� de la
    dur�e du son, voir sndinfo() dans le manuel.

"""
from pyo import *
import random
s = Server().boot()
sound = 'mus1323_test_1.wav'
info = sndinfo(sound)
lfo = Sine([.1, .15]).range(300, 3000)
amp = Fader(fadein=0.05, fadeout=0.05, dur=.035, mul=1, add=0)
player = SfPlayer(sound, speed=1, mul=amp)
filter = Biquad(player, freq=lfo, q=5, type=2, mul=1, add=0)
verb = Freeverb(filter, size=0.50, damp=0.50, bal=0.25, mul=1, add=0).out()
start = info[1] * 0.5
def function():
    global start
    player.offset = start
    player.play()
    amp.play()
    start += random.uniform(-0.03,0.03)
    
    if (start < 0.0 or start > info[1]):
        start = info[1]*0.5



pat = Pattern(function, time = .05).play()
    
    



 




s.gui(locals())