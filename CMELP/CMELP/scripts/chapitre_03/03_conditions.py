from pyo import *
s = Server().boot()

src = 1
fx = 0

if src == 0:
    source = Sine().out()
elif src == 1:
    source = FM().out()
elif src == 2:
    source = SineLoop().out()

source.ctrl()

if fx == 0:
    effet = Chorus(source).out(1)
elif fx == 1:
    effet = Harmonizer(source).out(1)
elif fx == 2:
    effet = Disto(source).out(1)
    
effet.ctrl()

s.gui(locals())