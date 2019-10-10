import random
from pyo import *

amps = []
frqs = []
fond = 80

for i in range(10):
    pit = random.uniform(30, 5000)
    frqs.append(pit)
    amp = (1 - ((pit - 30) / 4970)) ** 3
    amps.append(amp * 0.2)
    
print(amps)

s = Server().boot()
a = SineLoop(freq=frqs, mul=amps).out()
sp = Spectrum(a.mix(1))