from pyo import *
import random
s = Server().boot()

# env global
env = LinTable([(0,0), (150,1), (500,1), (5000,.5), (8191,0)], size=8192)
globmet = Metro(time=120).play()
globamp = TrigEnv(globmet, table=env, dur=120)


## ARP 01 1/64 à 90bpm
arp_noteTime = 0.0417
arp_notes = [midiToHz(x) for x  in [60 ,55 ,59 ,57]]
arp_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
arp_beat = Beat(time=arp_noteTime, taps=4, w1=80, w2=50, w3=30).play()
arp_trigChoice = TrigChoice(arp_beat, choice=arp_notes, port=0.005)
arp_amp = TrigEnv(arp_beat, table=arp_env, dur=arp_noteTime, mul=.5)

arp_instru = SuperSaw(freq=arp_trigChoice , detune=0, bal=0, mul=arp_amp).mix(2)
arp_Filter01 = ButLP(arp_instru, freq=2800)
arp_Chorus = Chorus(arp_Filter01, depth=1, feedback=0.25, bal=0.50)
arp_Verb = Freeverb(arp_Chorus, size=0.50, damp=0.50, bal=0.50)
arp_Filter02 = MoogLP(arp_Verb, freq=3200, res=.22, mul=.9*globamp).out()

## Pad 2/1 à 90bpm
pad_noteTime = 5.333
pad_notes = [midiToHz(x) for x  in [[48 ,55 ,60],[48 ,55 ,62],[48 ,53 ,62],[48 ,53 ,64]]]
pad_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
pad_beat = Beat(time=pad_noteTime, taps=4, w1=100, w2=100, w3=100).play()
pad_trigChoice = TrigChoice(pad_beat, choice=pad_notes, port=0.005)
pad_amp = TrigEnv(pad_beat, table=pad_env, dur=pad_noteTime, mul=.25)

pad_instru1 = SuperSaw(freq=pad_trigChoice , detune=0, bal=0, mul=pad_amp).mix(2)
pad_instru2 = SumOsc(freq=pad_trigChoice, ratio=0.50, index=0.50, mul=pad_amp*1.2).mix(2)
pad_Filter01 = MoogLP(pad_instru1, freq=1480, res=.22, mul=.9*globamp).out()
pad_Filter02 = ButBP(pad_instru2, freq=3000, mul=1*globamp).out()

## Bass 2/1 à 90bpm
bass_noteTime = 5.333
bass_notes = [midiToHz(x) for x  in [48,38,41,40]]

bass_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8190 ,.5) , (8191 ,0) ] , size =8192)
bass_beat = Beat(time=bass_noteTime, taps=4, w1=100, w2=100, w3=100).play()
bass_trigChoice = TrigChoice(bass_beat, choice=bass_notes, port=0.005)
bass_amp = TrigEnv(bass_beat, table=bass_env, dur=bass_noteTime, mul=.25)
fil_lfo = Sine(freq=1/bass_noteTime, phase=0, mul=1, add=0)

bass_instru = FM(carrier=bass_trigChoice, ratio=0.50, index=5, mul=bass_amp, add=0).mix(2)
bass_filter = MoogLP(bass_instru, freq=fil_lfo*300, res=.2, mul=.65*globamp, add=0).out()

## Misc
misc_noteTime = 0.0156*50 #peut-etre x5
misc_notes = [midiToHz(x) for x  in [71 ,67]]
misc_instu_env = ExpTable([ ( 0 , 0 ) , (400 ,1) , (500 ,1) , (1000 ,.5) , (5000 ,0) ] , size =8192)
misc_beat = Beat(time=misc_noteTime, taps=4, w1=100, w2=100, w3=0).play()
misc_trigChoice = TrigChoice(misc_beat, choice=misc_notes, port=0.005)
misc_amp = TrigEnv(misc_beat, table=misc_instu_env, dur=misc_noteTime, mul=1)

misc_instru = SuperSaw(freq=misc_trigChoice , detune=0, bal=0, mul=misc_amp).mix(2)
misc_Filter1 = ButLP(misc_instru, freq=1800, mul=1)
misc_Filter2 = ButHP(misc_Filter1, freq=800, mul=1)
misc_delay = Delay(misc_Filter2, delay=0.35, feedback=.75, maxdelay=1, mul=.5, add=0)
misc_chorus = Chorus([misc_Filter2,misc_delay], depth=1, feedback=0.25, bal=0.50, mul=1, add=0)
misc_verb = Freeverb(misc_chorus, size=1, damp=0.50, bal=0.50, mul=.5*globamp, add=0).out()






















#arp_Filter02.ctrl(title="Arp control")
#pad_Filter01.ctrl(title="pad 1")
#pad_Filter02.ctrl(title="pad 2")
#bass_filter.ctrl(title="bass")
#misc_verb.ctrl(title="misc")





#spectre = Spectrum(misc_Filter2, size=1024, wintype=2, function=None, wintitle="Spectrum")

s.gui(locals())