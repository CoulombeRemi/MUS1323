from pyo import *

# Petit exercice: Ajouter arguments et attributs (avec leur methode respective)
# pour controler le feedback du flange et son amplitude ("mul" serait un bon choix 
# de nom pour cet argument).

class Flanger:
    def __init__(self, input, freq=0.1, delay=0.005, depth=1):
        self.freq = Sig(freq)
        self.delay = Sig(delay)
        self.depth = Sig(depth)

        self.input = InputFader(input)

        self.lfo = Sine(self.freq, mul=self.delay*self.depth, add=self.delay)
        self.flange = Delay(self.input, delay=self.lfo, add=self.input)

    def sig(self):
        return self.flange

    def out(self):
        self.flange.out()
        return self

    def setInput(self, x, fadetime=0.05):
        self.input.setInput(x, fadetime)

    def setFreq(self, x):
        self.freq.value = x

    def setDelay(self, x):
        self.delay.value = x

    def setDepth(self, x):
        self.depth.value = x

s = Server().boot()

n = Noise(.05)
sf = SfPlayer(SNDS_PATH + "/transparent.aif", loop=True, mul=0.4)
f = Flanger(n, freq=.1, delay=0.003, depth=1)
rev = STRev(f.sig(), bal=0.2).out()

f.setInput(sf, 30)

s.gui(locals())