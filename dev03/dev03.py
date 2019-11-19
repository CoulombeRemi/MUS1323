from pyo import *
import random
s = Server().boot()

## ARP 01
arp_notes = [midiToHz(x) for x  in [60 ,55 ,59 ,57]]
arp_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
# 1/64 à 90bpm
arp_noteTime = 0.0417
arp_beat = Beat(time=arp_noteTime, taps=4, w1=80, w2=50, w3=30).play()
arp_trigChoice = TrigChoice(arp_beat, choice=arp_notes, port=0.005)

arp_amp = TrigEnv(arp_beat, table=arp_env, dur=arp_noteTime, mul=.5)
arp_instru = SuperSaw(freq=arp_trigChoice , detune=0, bal=0, mul=arp_amp).mix(2)
arp_Filter01 = ButLP(arp_instru, freq=2800)
arp_Chorus = Chorus(arp_Filter01, depth=1, feedback=0.25, bal=0.50)
arp_Verb = Freeverb(arp_Chorus, size=0.50, damp=0.50, bal=0.50)
arp_Filter02 = MoogLP(arp_Verb, freq=3500, res=.22, mul=1).out()



## Pad
pad_notes = [midiToHz(x) for x  in [[48 ,55 ,60],[48 ,55 ,62],[48 ,53 ,62],[48 ,53 ,64]]]
pad_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
# 2/1 à 90bpm
pad_noteTime = 5.333
pad_beat = Beat(time=pad_noteTime, taps=4, w1=100, w2=100, w3=100).play()
pad_trigChoice = TrigChoice(pad_beat, choice=pad_notes, port=0.005)
pad_amp = TrigEnv(pad_beat, table=pad_env, dur=pad_noteTime, mul=.25)
pad_instru = SuperSaw(freq=pad_trigChoice , detune=0, bal=0, mul=pad_amp).mix(2).out()



s.gui(locals())

Counter(input, min=0, max=100, dir=0, mul=1, add=0)