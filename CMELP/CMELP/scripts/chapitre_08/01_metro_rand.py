from pyo import *

s = Server().boot()

# Ne pas oublier d'appeler la methode .play() pour les objets Metro et Beat
met = Metro(time=.125).play()
t = TrigRand(met, min=400, max=1000)
a = SineLoop(freq=t, feedback=0.05, mul=.3).out()

s.gui(locals())