from pyo import *



class Waha:
    def __init__(self, son, min, max, que):
        ampToFrq = amp*20000    
        self.filter = ButBP(son, freq=ampToFrq, q=que, mul=0.4, add=0)

        if(ampToFrq < min):
            print("min")
            self.filter.freq = min
        if(ampToFrq > max):
            print("max")
            self.filter.freq = max


        print(self.filter.freq)
            

    def out(self, chnl=0):
        self.filter.out()
        return self
        
    def sig(self):
        return self.filter
        

s = Server().boot()

sf = SfPlayer("drum.wav", speed=1, loop=True, mul=1)
amp = PeakAmp(sf)

sf.out()

 
output = Waha(sf, 500, 2000, 6).out()
output.filter.ctrl()
    

#p = Print(amp, method=0, interval=.05, message="RMS")
s.gui(locals())
