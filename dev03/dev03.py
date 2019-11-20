from pyo import *
import random
s = Server().boot()


    





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
arp_Filter02 = MoogLP(arp_Verb, freq=3500, res=.22, mul=1).out()


## Pad 2/1 à 90bpm
pad_noteTime = 5.333
pad_notes = [midiToHz(x) for x  in [[48 ,55 ,60],[48 ,55 ,62],[48 ,53 ,62],[48 ,53 ,64]]]
pad_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
pad_beat = Beat(time=pad_noteTime, taps=4, w1=100, w2=100, w3=100).play()
pad_trigChoice = TrigChoice(pad_beat, choice=pad_notes, port=0.005)
pad_amp = TrigEnv(pad_beat, table=pad_env, dur=pad_noteTime, mul=.25)

pad_instru1 = SuperSaw(freq=pad_trigChoice , detune=0, bal=0, mul=pad_amp).mix(2)
pad_instru2 = SumOsc(freq=pad_trigChoice, ratio=0.50, index=0.50, mul=pad_amp*1.2).mix(2)
pad_Filter01 = MoogLP(pad_instru1, freq=2000, res=.22, mul=1).out()
pad_Filter02 = ButBP(pad_instru2, freq=2500).out()

## Bass 2/1 à 90bpm
bass_noteTime = 5.333
bass_notes = [midiToHz(x) for x  in [48 ,38 ,41 ,40]]
bass_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8190 ,.5) , (8191 ,0) ] , size =8192)
bass_beat = Beat(time=bass_noteTime, taps=4, w1=100, w2=100, w3=100).play()
bass_trigChoice = TrigChoice(bass_beat, choice=bass_notes, port=0.005)
bass_amp = TrigEnv(bass_beat, table=bass_env, dur=bass_noteTime, mul=.25)

fil_lfo = Sine(freq=0.5/bass_noteTime, phase=0, mul=1, add=0)
bass_instru = FM(carrier=bass_trigChoice, ratio=0.50, index=5, mul=bass_amp, add=0).mix(2).out()
#bass_filter = MoogLP(bass_instru, freq=fil_lfo*1000, res=0, mul=1, add=0).out()


#spectre = Spectrum(bass_filter, size=1024, wintype=2, function=None, wintitle="Spectrum")

s.gui(locals())