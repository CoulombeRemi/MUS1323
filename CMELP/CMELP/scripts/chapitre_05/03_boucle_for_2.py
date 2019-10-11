"""
Exercice boucle "for", version 2, serie de frequences et d'amplitudes.

"""
from pyo import *
import random

s = Server().boot()

freqs = []
amps = []

fond = 50
for i in range(1,21):
    dev = random.uniform(.98,1.02)
    freqs.append(i*fond*dev)
    amps.append(0.35/i)

print('Frequences : ', freqs)
print('Amplitudes : ', amps)
        
a = Sine(freq=freqs, mul=amps).out()    

s.gui(locals())

