from pyo import *
import os

# Remi Coulombe 20130013
# 4 decembre 2019
# TP04 - MUS1323

class Waha:
    def __init__(self, son, min=20, max=20000, cutFrq=30, que=3):
        self.son = son
        self.min = Sig(min) # minimal frq 
        self.max = Sig(max) # maximal frq 
        self.cutFrq = Sig(cutFrq) # cut frq
        self.que = Sig(que) # Q
        self.amp = Follower(self.son, freq=self.cutFrq)
        ampToFrq = self.amp * (self.max - self.min) + self.min
        self.filter = ButBP(self.son, freq=ampToFrq, q=self.que, mul=1)

    ## set new freq. to sig(value)
    def min_frq(self, min_newFq):
        self.min.value = min_newFq
    def max_frq(self, max_newFq):
        self.max.value = max_newFq
    def cut_frq(self, cut_newFq):
        self.cutFrq.value = cut_newFq
    def cut_frq(self, new_Q):
        self.que.value = new_Q
        
    def out(self):
        self.filter.out()
        return self
        
    def sig(self):
        return self.filter
        

s = Server().boot()
path = os.path.join(os.path.expanduser("~"), "Desktop", "wahaDrum_fullWet.wav") # settings utilises: Waha(sf, 200, 16000, 20, 2.6)
s.recordOptions(dur=10, filename=path, fileformat=0, sampletype=0)

sf = SfPlayer("drum_dry.wav", loop=True, mul=1)#.out()
output = Waha(sf, 200, 16000, 20, 2.6).out()
#output.min_frq(3000)
#output.cut_frq(2)


output.filter.ctrl()
#s.recstart()
s.gui(locals())
