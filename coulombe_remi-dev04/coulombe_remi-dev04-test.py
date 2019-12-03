from pyo import *



class Waha:
    



    def __init__(self, son, min, max, que):
        self.ampToFrq = amp*20000
        self.min = min
        self.max = max
        self.filter = ButBP(son, freq=self.min_max(), q=que, mul=0.75, add=0)
        
        p = Print(amp, method=0, interval=0.25, message="ampToFrq: ")
        
    # https://stackoverflow.com/questions/5996881/how-to-limit-a-number-to-be-within-a-specified-range-python
    def min_max(self):
        if self.ampToFrq < self.min:
            print("mini")
            return self.min
        elif self.ampToFrq > self.max:
            print("maxi")
            return self.max
        else:
            print("same")
            return self.ampToFrq
            
    # https://stackoverflow.com/questions/32447397/how-to-check-if-a-variables-value-has-changed/38143715#38143715

            

    #print(min_max(10, 1, 25))


    def out(self, chnl=0):
        self.filter.out()
        return self
        
    def sig(self):
        return self.filter
        

s = Server().boot()

sf = SfPlayer("drum.wav", speed=1, loop=True, mul=1)
amp = PeakAmp(sf) ## get peak amplitude from sound file
#sf.out()





 
output = Waha(sf, -100, 50000, 6).out() # pass arg. to class and output it
output.filter.ctrl() # access filter controls from class Waha


# p = Print(amp, method=0, interval=0.025, message="RMS")
s.gui(locals())
