#!/usr/bin/env python
# encoding: utf-8
"""
Solution pour l'exercice 1 sur les 'lists comprehension'.

"""
from pyo import *
from random import uniform

s = Server().boot()

sf = SfPlayer(SNDS_PATH+'/transparent.aif', loop=True, mul=.07,
              speed=[uniform(.99,1.01) for i in range(10)]).mix(1)
sf.out()
harm = Harmonizer(sf, transpo=[-12,7,4], mul=.4).out(1)

s.gui(locals())