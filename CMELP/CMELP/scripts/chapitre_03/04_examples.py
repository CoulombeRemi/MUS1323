"""
Exemples de chaines de traitement. Aucun parametres a l'initialisation.
Exploration avec la fenetre 'ctrl'.

Exemple no 1 : Connections en cascade :
    sine  ->  disto  ->  chorus

Exemple no 2 : Connections en parallele (multi-effets) :
    sineloop  ->  freqshift
              ->  freqshift

Exemple no 3 : Connections en parallele (multi-sources) :
    lfo 1  ->
    lfo 2  ->  harmonizer
    lfo 3  ->

"""
from pyo import *

s = Server(audio='portaudio').boot()
s.amp = .1 # initialise le serveur a -20 dB

exemple = 3 # modifier cette variable pour changer d'exemple

if exemple == 1:
    src = Sine()
    src.ctrl()
    dist = Disto(src)
    dist.ctrl()
    chor = Chorus(dist).out()
    chor.ctrl()
elif exemple == 2:
    src = SineLoop()
    src.ctrl()
    fshif = FreqShift(src).out()
    fshif.ctrl()
    fshif2 = FreqShift(src).out(1)
    fshif2.ctrl()
elif exemple == 3:
    src1 = LFO().out()
    src1.ctrl()
    src2 = LFO().out()
    src2.ctrl()
    src3 = LFO().out()
    src3.ctrl()
    harm = Harmonizer(src1+src2+src3).out(1)
    harm.ctrl()

s.gui(locals())
