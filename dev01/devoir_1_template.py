# encoding: utf-8
"""
MUS-1323 - devoir 1

Construire une petit boîte à effet.

Un signal monophonique en provenance du micro doit d'abord
être distortionné, puis envoyé dans deux délais récursifs 
en parallèle. Le signal de sortie de chacun des délais doit 
ensuite être transposé puis envoyé à son haut-parleur désigné, 
le premier délai transposé à gauche, le second à droite.

On veut aussi entendre la source originale au centre des deux
haut-parleurs.

Le premier délai doit retarder le son de 100 ms et le second de
200 ms. Ajoutez aussi un peu de récursion (50%).

La transposition du canal de gauche est de 1 demi-ton vers le bas
tandis que la transposition du canal de droite est de 1 demi-ton
vers le haut.

Ajustez les amplitudes pour obtenir un niveau confortable!

==================== Schéma de connection ============================
input --> distorsion --> delai 1 --> transposition 1 --> sortie gauche 
  |                  --> delai 2 --> transposition 2 --> sortie droite
  |
  | --> sortie gauche
  | --> sortie droite

"""
from pyo import *

s = Server().boot()

src = Input()



s.gui(locals())
