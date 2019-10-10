#!/usr/bin/env python
# encoding: utf-8
"""
Cours 4 - exercice boucle "for", FM synth.

"""
from pyo import *
import random

s = Server().boot()

car = []
rat = []
ind = []
for i in range(10):
    car.append(random.triangular(150, 155))
    rat.append(random.choice([.25, .5, 1, 1.25, 1.5, 2]))
    ind.append(random.randint(2, 6))
 
print('Carrier : ', car)
print('Ratio : ', rat)
print('Index : ', ind)
    
fm = FM(carrier=car, ratio=rat, index=ind, mul=.05).out()
    
s.gui(locals())
