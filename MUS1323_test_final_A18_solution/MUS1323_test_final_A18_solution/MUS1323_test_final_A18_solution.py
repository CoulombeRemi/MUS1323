"""
MUS1323 - Examen final - Automne 2018

La flûte et le canon...

1 - Vous devez créer une classe permettant d'appliquer un délai et
de transposer un signal audio donné en entrée. Le signal délayé et
transposé doit ensuite être panoramisé dans l'espace stéréo.

2 - On veut pouvoir spécifier le temps de délai, le facteur de
transposition et la panoramisation en arguments à l'initialisation
de la classe.

3 - Vous devez ensuite faire jouer en boucle, à sa hauteur originale,
le son "flute_irlandaise.aif". Ce signal servira de source audio à
3 objets de la classe précédemment définie.

4 - Les temps de délai et les facteurs de transposition doivent être
répartis comme ceci (assurez-vous que les temps de délai sont bel et 
bien respectés):

    - délai: 1/4 de la durée du son source, transpo: quinte en dessous
    - délai: 1/2 de la durée du son source, transpo: quarte au dessus 
    - délai: 3/4 de la durée du son source, transpo: octave en dessous

5 - Chacun des quatres signaux (l'original et les trois délais) doivent
être positionnés à un endroit différent de l'espace stéréo.

"""
from pyo import *

s = Server().boot()

source = "flute_irlandaise.aif"

dur = sndinfo(source)[1]

class DelTrans:
    def __init__(self, input, deltime=0.1, transpo=-7, pan=0.5):
        self.input = InputFader(input)
        self.delay = Delay(self.input, delay=deltime, maxdelay=dur)
        self.harmo = Harmonizer(self.delay, transpo=transpo)
        self.panner = Pan(self.harmo, pan=pan).out()

sf = SfPlayer(source, loop=True, mul=0.3)
sfpan = Pan(sf, pan=0.6).out()

a = DelTrans(sf, dur*0.25, transpo=-7, pan=0.1)
b = DelTrans(sf, dur*0.5, transpo=5, pan=0.9)
c = DelTrans(sf, dur*0.75, transpo=-12, pan=0.3)

s.gui(locals())
