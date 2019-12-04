from pyo import *

# Rémi Coulombe 20130013
# 3 décembre 2019
# TP04 - MUS1323

class Waha:
    def __init__(self, son, min, max, que):
        self.ampToFrq = amp * (max - min) + min # define the range between the min and max
        self.filter = ButBP(son, freq=self.ampToFrq, q=que, mul=0.75, add=0)

    
    def out(self, chnl=0):
        self.filter.out()
        return self
        
    def sig(self):
        return self.filter
        

s = Server().boot()

sf = SfPlayer("drum.wav", speed=1, loop=True, mul=1)
amp = PeakAmp(sf) ## get peak amplitude from sound file
sf.ctrl()
sf.out()



output = Waha(sf, 500, 1000, 6).out() # pass arg. to class and output it

output.filter.ctrl() # access filter controls from class Waha

p = Print(output.ampToFrq, method=0, interval=0.25, message="Waha frq")


s.gui(locals())
