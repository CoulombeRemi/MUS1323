# Exercice boucle "for", serie de frequences et d'amplitudes.
from pyo import *

s = Server().boot()

freqs = []
amps = []

fond = 50
for i in range(1,21):
    freqs.append(i*fond)
    amps.append(0.35/i)

print('Frequences : ', freqs)
print('Amplitudes : ', amps)
        
a = Sine(freq=freqs, mul=amps).out()

s.gui(locals())

