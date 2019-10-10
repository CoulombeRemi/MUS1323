"""
Specification des arguments a l'initialisation des objets.

Trois sonorites sur la base de l'exemple no 3 du cours precedent :
----------------------------------------------------
Exemple no 3 : Connections en parallele (multi-sources) :
    lfo 1  ->
    lfo 2  ->  harmonizer
    lfo 3  ->
----------------------------------------------------

Exemple no 1 : 
    Accord consonant avec une legere deviation des frequences
    pour creer un effet de modulation.

Exemple no 2 :
    Frequences des LFOs tres rapprochees et harmonisation de
    1/10e de demi-ton avec feedback pour creer un effet de flange.

Exemple no 3 :
    Desaccord total, sonorite se rapprochant du bruit.

"""
from pyo import *

s = Server().boot()

exemple = 1 # modifier cette variable pour changer d'exemple

if exemple == 1:
    src1 = LFO(freq=100, sharp=.5, mul=.1).out()
    src2 = LFO(freq=150.5, sharp=.25, mul=.1).out()
    src3 = LFO(freq=200.78, sharp=.15, mul=.1).out()
    harm = Harmonizer(src1+src2+src3, transpo=-7).out(1)
elif exemple == 2:
    src1 = LFO(freq=100, sharp=.75, mul=.1).out()
    src2 = LFO(freq=99.8, sharp=.75, mul=.1).out()
    src3 = LFO(freq=100.3, sharp=.75, mul=.1).out()
    harm = Harmonizer(src1+src2+src3, transpo=0.1, feedback=.8, mul=.6).out(1)
elif exemple == 3:
    src1 = LFO(freq=100, sharp=.75, mul=.1).out()
    src2 = LFO(freq=123, sharp=.65, mul=.1).out()
    src3 = LFO(freq=178, sharp=.5, mul=.1).out()
    harm = Harmonizer(src1+src2+src3, transpo=2.33, feedback=.5).out(1)

s.gui(locals())
