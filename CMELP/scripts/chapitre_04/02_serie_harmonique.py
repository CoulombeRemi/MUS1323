from pyo import *
s = Server().boot() 
a = Sine(freq=list(range(100,1000,100)),
         mul=[.5,.35,.2,.14,.1,.07,.05,.03,.01]).out()
s.gui(locals())
