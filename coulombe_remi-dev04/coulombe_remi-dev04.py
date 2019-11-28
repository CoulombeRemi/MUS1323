from pyo import *



class Waha:
    def __init__(self, son, frqCut, min, max, que):
        self.filter = ButBP(son, freq=fol*10000, q=que, mul=0.4, add=0)
        
    def out(self, chnl=0):
        self.filter.out()
        return self
        
    def sig(self):
        return self.filter
        
    print("allo")

s = Server().boot()

sf = SfPlayer("drum.wav", speed=1, loop=True, mul=0.4)
fol = Follower(sf, freq=20, mul=1, add=0)



output = Waha(sf, 200, 20, 2000, 6).out()
output.filter.ctrl()




#p = Print(fol, method=0, interval=.1, message="RMS")
s.gui(locals())
