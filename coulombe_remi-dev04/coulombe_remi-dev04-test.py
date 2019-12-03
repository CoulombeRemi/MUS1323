from pyo import *

# Rémi Coulombe 20130013
# 3 décembre 2019
# TP04 - MUS1323

class Waha:
    def __init__(self, son, min, max, que):
        ampToFrq = amp * (max - min) + min # define the range between the min and max
        self.filter = ButBP(son, freq=ampToFrq, q=que, mul=0.75, add=0)
        
    # https://stackoverflow.com/questions/5996881/how-to-limit-a-number-to-be-within-a-specified-range-python
    #def min_max(self):
        #if self.ampToFrq < self.min:
        #    print("mini")
        #    return self.min
        #elif self.ampToFrq > self.max:
        #    print("maxi")
        #    return self.max
        #else:
        #    print("same")
        #    return self.ampToFrq
            
    # https://stackoverflow.com/questions/32447397/how-to-check-if-a-variables-value-has-changed/38143715#38143715

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



output = Waha(sf, 20, 20000, 6).out() # pass arg. to class and output it
output.filter.ctrl() # access filter controls from class Waha



s.gui(locals())
