# on importe tous les éléments de la librairie pyo
from pyo import*

# obligatoir avec pyo.
# on demarre le serveur avec boot() qui est une fonction de serveur
s = Server().boot()
s.start()
# objet sonore
#sine = CrossFM().out()
# controleur de frq, phase, et mul
#sine.ctrl()

notes = Notein(poly=10, scale=1, mul=0.2).out()
Notein.keyboard(title="Notein keyboard", wxnoserver=False)

notes.ctrl()





# Graph pour voir les frq
sp = Spectrum(notes)

# fenetre graphique
s.gui(locals())