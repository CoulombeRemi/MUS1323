from pyo import *
import random

s = Server().boot()

fm = FM(carrier=[random.triangular(150, 155) for i in range(10)], 
        ratio=[random.choice([.25, .5, 1, 1.25, 1.5, 2]) for i in range(10)], 
        index=[random.randint(2, 6) for i in range(10)], mul=.05).out()

s.gui(locals())
