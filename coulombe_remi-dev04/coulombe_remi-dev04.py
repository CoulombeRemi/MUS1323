from pyo import *

s = Server().boot()

class Waha:
    def __init__(self, frqCut, min, max, q):
        self.filter = ButBP(sf, freq=fol*10000, q=self.q, mul=0.4, add=0)
        
    def out(self, chnl=0):
        self.filter.out()
        return self
        
    def sig(self):
        return self.filter


sf = SfPlayer("drum.wav", speed=1, loop=True, mul=0.4)
fol = Follower(sf, freq=20, mul=1, add=0)


filter.ctrl()



p = Print(fol, method=0, interval=.1, message="RMS")
s.gui(locals())
