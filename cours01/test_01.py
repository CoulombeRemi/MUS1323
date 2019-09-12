# on importe tous les éléments de la librairie pyo
from pyo import*

# obligatoir avec pyo.
# on demarre le serveur avec boot() qui est une fonction de serveur
s = Server().boot()

# objet sonore
lfo = Sine(freq=4, mul=58, add=500)
sine = Sine(freq=lfo).out()

# fenetre graphique
s.gui(locals())