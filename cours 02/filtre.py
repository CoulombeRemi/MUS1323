from pyo import *
s = Server().boot()
s.amp(0.1)
a = SumOsc()
a.ctrl()
b = ButLP(a)
b.ctrl
c = Chorus(b)
c.ctrl()
s.gui(locals())
