"""
MUS1323 - Examen final - Automne 2017

Les délais filtrés en parallèle

Vous devez créer un traitement multi-bande appliqué à une source sonore.

1 - Le traitement, pour une bande de fréquence, doit être créer à 
    l'intérieur d'une classe. Il doit mettre en place un filtre 
    passe-bande, suivi d'un délai puis d'une modulation d'amplitude.
    On veut entendre uniquement la sortie de la modulation d'amplitude.

    FILTRE PASSE_BANDE ==> DELAI ==> MODULATION AMPLITUDE ==> OUT

2 - Votre classe doit recevoir en arguments: Le signal audio à traiter,
    la fréquence centrale du filtre, le Q du filtre, le temps de délai
    en seconde, la fréquence de modulation et le canal audio où le signal
    doit être envoyé.

3 - Utiliser une lecture en boucle du son "pouf_chips.aiff" comme signal
    audio à traiter par 6 instances de votre classe. Trois instances doivent 
    jouer à gauche et les trois autres à droite. Les paramètres doivent être 
    différents pour chaque instance.

"""

class BPFilterAm:
    def __init__(self, input, fCentrale=1000, fQ=2, delai=0.25, fModul=0.1, chnl=0): #arguments de départ
        self.input = input                  #signal audio à traiter
        self.fCentrale = Sig(fCentrale)     #fréquence centrall du filtre
        self.fQ = Sig(fQ)                   #Q du filtre
        self.delai = Sig(delai)             #temps de délai
        self.fModul = Sig(fModul)           #fréquence de modulation pour modulation d'amplitude
        self.chnl = chnl                    #canal audio 
        
        #différents modules et chemin du signal
        self.bandPass = Biquad(self.input.mix(1), freq=self.fCentrale, q=self.fQ, type=2)
        self.delay= Delay(self.bandPass, delay=self.delai, feedback=0, maxdelay=3)
        self.am = Sine(freq=self.fModul)
        self.signalOut= self.delay * self.am    #modulation d'amplitude
        #mise en place de la condition left/right
        if self.chnl == 0:
            self.signalOut.out()
        elif self.chnl == 1:
            self.signalOut.out(1)

from pyo import *

source = 'pouf_chips.aiff'  #appel simple car le fichier son est sauvegardé dans le même dossier que le projet

s = Server().boot()

_player = SfPlayer(source, speed=1, loop=True, offset=0, interp=2, mul=1, add=0)    #loop (True)

#canal de gauche
_filter01 = BPFilterAm(_player, fCentrale=100, fQ=4, delai=2, fModul=0.01, chnl=0)
_filter02 = BPFilterAm(_player, fCentrale=3000, fQ=2, delai=1, fModul=0.1, chnl=0)
_filter03 = BPFilterAm(_player, fCentrale=6000, fQ=1, delai=4, fModul=0.2, chnl=0)
#canal de droite
_filter04 = BPFilterAm(_player, fCentrale=500, fQ=3, delai=5, fModul=0.15, chnl=1)
_filter05 = BPFilterAm(_player, fCentrale=4000, fQ=5, delai=6, fModul=0.25, chnl=1)
_filter06 = BPFilterAm(_player, fCentrale=8000, fQ=1.5, delai=1.5, fModul=0.3, chnl=1)

s.gui(locals())
