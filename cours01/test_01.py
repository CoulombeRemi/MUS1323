# on importe tous les éléments de la librairie pyo
from pyo import*

# obligatoir avec pyo.
# on demarre le serveur avec boot() qui est une fonction de serveur
s = Server().boot()

# objet sonore
sine = Sine().out()
# controleur de frq, phase, et mul
sine.ctrl()

# fenetre graphique
s.gui(locals())