"""
Elargissement des sonorites a l'aide de listes en argument,
sur la base des trois sonorites de l'exemple precedent.

Exemple no 1 : 
    Chorus sur chaque sources + multiples harmonisations.
Exemple no 2 :
    Frequences des LFOs tres rapprochees, sur 3 frequences
    et legeres harmonisations avec feedback pour creer un 
    effet de flange.
Exemple no 3 :
    Desaccord total, encore plus proche du bruit.
"""
from pyo import *

s = Server().boot()

exemple = 1 # modifier cette variable pour changer d'exemple

if exemple == 1:
    s1 = LFO(freq=[100,100.03,99.95,99.91], sharp=.5, mul=.05).out()
    s2 = LFO(freq=[150.41,150.5,150.78,150.98], sharp=.25, mul=.05).out()
    s3 = LFO(freq=[200.78,201,201.3,202.1], sharp=.15, mul=.05).out()
    h = Harmonizer(s1+s2+s3, transpo=[-12,-7,5,7], mul=[1,.7,.5,.4]).out()
elif exemple == 2:
    s1 = LFO(freq=[100,300,500], sharp=.75, mul=[.1,.02,.015]).out()
    s2 = LFO(freq=[99.8, 300.3,500.5], sharp=.75, mul=[.1,.02,.015]).out()
    s3 = LFO(freq=[100.3,299.76,499,65], sharp=.75, mul=[.1,.02,.015]).out()
    h = Harmonizer(s1+s2+s3, transpo=[-.07,.04,.1], feedback=.8, mul=.4).out(1)
elif exemple == 3:
    s1 = LFO(freq=[100,276,421,511], sharp=.75, mul=[.1,.03,.02,.01]).out()
    s2 = LFO(freq=[123,324,389,488], sharp=.65, mul=[.1,.03,.02,.01]).out()
    s3 = LFO(freq=[178,265,444,561], sharp=.5, mul=[.1,.03,.02,.01]).out()
    h = Harmonizer(s1+s2+s3, transpo=[-3.76,2.33], feedback=.5).out(1)

s.gui(locals())
