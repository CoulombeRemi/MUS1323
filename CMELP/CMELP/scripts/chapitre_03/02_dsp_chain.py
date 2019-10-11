from pyo import *
s = Server().boot()
fm = FM()
fm.ctrl()
filt = ButLP(fm).out()
filt.ctrl()
harmo = Harmonizer(filt).out(1)
harmo.ctrl()
s.gui(locals())