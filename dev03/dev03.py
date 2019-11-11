from pyo import *
s = Server().boot()


def bass()
    


bassNotes = [16, 22]
bass = RCOsc(freq=bassNotes, sharp=1, mul=.3, add=0)
#bassNoise = Noise(mul=.01, add=0)
BassSub = Sine(freq=bassNotes, phase=0, mul=.5, add=0)
bassFilter = MoogLP([bass,BassSub], freq=30, res=39, mul=1, add=0)
bassEq = EQ(bassFilter, freq=255, q=.7, boost=-12, type=0, mul=1, add=0).out()


pattern = Pattern(bass, time=1, arg=None).play()













spectre = Spectrum([bass,BassSub,bassEq], size=1024, wintype=2, function=None, wintitle="Spectrum")
s.gui(locals())