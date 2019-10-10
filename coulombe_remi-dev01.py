from pyo import *
s = Server().boot()
s.amp = 0.07

# Main source
src = Input().mix(2).out()

# Effects
disto = Disto(src, drive=0.75, slope=0.50, mul=1, add=0)
disto.ctrl()

delayL = Delay(disto, delay=0.1, feedback=0.5, maxdelay=1, mul=1, add=0)
delayR = Delay(disto, delay=0.2, feedback=0.5, maxdelay=1, mul=1, add=0)

transpoL = Harmonizer(delayL, transpo=-1).out(0)
transpoR = Harmonizer(delayR, transpo=1).out(1)

# //////////////
s.gui(locals())