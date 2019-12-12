"""
Remi Coulombe - 20130013
exam final mus1323
12/12/2019
"""

from pyo import *

class ModRing:
    def __init__(self,src, ratio = 1, bal = 10, waveShape = 0):
        self.src = src # input signal
        self.ratio = Sig(ratio)
        self.bal = Sig(bal)
        self.wave = waveShape
        self.pitchInput = Yin(self.src, tolerance=0.20, minfreq=20, maxfreq=20000, cutoff=18000, winsize=1024, mul=1) # input signal frq.
        freq = self.ratio*self.pitchInput
        # choix wave
        if self.wave == 0:
            print("Sine")
            self.osc = Sine(freq=freq, phase=0, mul=1, add=0)
        else:
            print("Saw")
            self.osc = SuperSaw(freq=freq)
        self.balance = Balance(self.src, self.osc, freq=bal, mul=0.1)
            
    def setRatio(self, newRatio):
        self.ratio.value = newRatio
        
    def setBalance(self, newBal):
        self.bal.value = newBal
        
    def out(self):
        self.balance.out()
        return self

    def Sig(self):
        return self.balance
        

s = Server().boot()

sf = SfPlayer("flute_irlandaise.aif", loop=True, mul=0.3)
## soundFile, ratio, balance (0-100), waveShape (0 ou 1)
modulation = ModRing(sf, 1, 100, 0).out()
s.gui(locals())