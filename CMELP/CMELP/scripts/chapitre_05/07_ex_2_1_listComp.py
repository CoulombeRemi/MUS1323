#!/usr/bin/env python
# encoding: utf-8
"""
Solution pour l'exercice 2.1 sur les 'lists comprehension'.

"""
from pyo import *
from random import uniform

s = Server().boot()

max_harms = 20
freqs = [i * 100 for i in range(max_harms) if (i%2) == 1]
amps = [0.35 / i for i in range(max_harms) if (i%2) == 1]
print("Frequences :", freqs)
print("Amplitudes :", amps)
a = Sine(freq=freqs, mul=amps).mix(1).out()

s.gui(locals())