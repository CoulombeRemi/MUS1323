# encoding: utf-8
# Rémi Coulombe 20130013
# tp03 20 nov. 2019

from pyo import *
import random
s = Server().boot()

# env global
env = LinTable([(0,0), (150,1), (500,1), (5000,.5), (8191,0)], size=8192)
globmet = Metro(time=120).play()
globamp = TrigEnv(globmet, table=env, dur=120)

# 90 bpm notes speed
noteSpeed = {"sixFour":0.0417, "twoOne":5.333, "oneOne":0.667, "douzHui":1}

i = 1
def chords():
    global i
    global melo_trigChoice
    k = (i/2)%2
    if k==0:
        melo_trigChoice.choice = [midiToHz(x) for x  in melo_notes["octTwo"]]
    elif k==1:
        melo_trigChoice.choice = [midiToHz(x) for x  in melo_notes["octThr"]]
    else :
        melo_trigChoice.choice = [midiToHz(x) for x  in melo_notes["octOne"]]
    print(melo_trigChoice.choice)
    i+=1
    if i > 10 : 
        melo_trigChoice.choice = [0]
    
## Arp
arp_notes = [midiToHz(x) for x  in [60 ,55 ,59 ,57]]
arp_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
arp_beat = Beat(time=noteSpeed["sixFour"], taps=4, w1=80, w2=50, w3=30).play()
arp_trigChoice = TrigChoice(arp_beat, choice=arp_notes, port=0.005)
arp_amp = TrigEnv(arp_beat, table=arp_env, dur=noteSpeed["sixFour"], mul=.5)

arp_instru = SuperSaw(freq=arp_trigChoice , detune=0, bal=0, mul=arp_amp).mix(2)
arp_Filter01 = ButLP(arp_instru, freq=2800)
arp_Chorus = Chorus(arp_Filter01, depth=1, feedback=0.25, bal=0.50)
arp_Verb = Freeverb(arp_Chorus, size=0.50, damp=0.50, bal=0.50)
arp_Filter02 = MoogLP(arp_Verb, freq=4200, res=.22, mul=.9*globamp).out()

## Misc
misc_notes = [midiToHz(x) for x  in [71 ,67]]
misc_instu_env = ExpTable([ ( 0 , 0 ) , (400 ,1) , (500 ,1) , (1000 ,.5) , (5000 ,0) ] , size =8192)
misc_beat = Beat(time=noteSpeed["douzHui"], taps=4, w1=100, w2=100, w3=0).play()
misc_trigChoice = TrigChoice(misc_beat, choice=misc_notes, port=0.005)
misc_amp = TrigEnv(misc_beat, table=misc_instu_env, dur=noteSpeed["douzHui"], mul=1)

misc_instru = SuperSaw(freq=misc_trigChoice , detune=0, bal=0, mul=misc_amp).mix(2)
misc_Filter1 = ButLP(misc_instru, freq=1800, mul=1)
misc_Filter2 = ButHP(misc_Filter1, freq=800, mul=1)
misc_delay = Delay(misc_Filter2, delay=0.35, feedback=.75, maxdelay=1, mul=.75, add=0)
misc_chorus = Chorus([misc_Filter2,misc_delay], depth=1, feedback=0.25, bal=0.50, mul=1, add=0)
misc_verb = Freeverb(misc_chorus, size=1, damp=0.50, bal=0.50, mul=.5*globamp, add=0).out()

## Pad
pad_notes = [midiToHz(x) for x  in [[48 ,55 ,60],[48 ,55 ,62],[48 ,53 ,62],[48 ,53 ,64]]]
pad_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8000 ,.5) , (8191 ,0) ] , size =8192)
pad_beat = Beat(time=noteSpeed["twoOne"], taps=4, w1=100, w2=100, w3=100).play(delay=noteSpeed["twoOne"]*2)
pad_trigChoice = TrigChoice(pad_beat, choice=pad_notes, port=0.005)
pad_amp = TrigEnv(pad_beat, table=pad_env, dur=noteSpeed["twoOne"], mul=.25)

pad_instru1 = SuperSaw(freq=pad_trigChoice , detune=0, bal=0, mul=pad_amp).mix(2)
pad_instru2 = SumOsc(freq=pad_trigChoice, ratio=0.50, index=0.5, mul=pad_amp*1.2).mix(2)
pad_Filter01 = MoogLP(pad_instru1, freq=1480, res=.22, mul=.9*globamp)
pad_Filter02 = ButBP(pad_instru2, freq=3000, mul=1*globamp)
pad_verb = Freeverb([pad_Filter01,pad_Filter02], size=0.50, damp=0.50, bal=0.50, mul=1, add=0).out()

## Bass
bass_notes = [midiToHz(x) for x  in [48,38,41,40]]
bass_env = ExpTable([ ( 0 , 0 ) , (100 ,1) , (500 ,.5) , (8190 ,.5) , (8191 ,0) ] , size =8192)
bass_beat = Beat(time=noteSpeed["twoOne"], taps=4, w1=100, w2=100, w3=100).play(delay=noteSpeed["twoOne"]*4)
bass_trigChoice = TrigChoice(bass_beat, choice=bass_notes, port=0.005)
bass_amp = TrigEnv(bass_beat, table=bass_env, dur=noteSpeed["twoOne"], mul=.25)
fil_lfo = Sine(freq=1/noteSpeed["twoOne"], phase=0, mul=1, add=0)

bass_instru = FM(carrier=bass_trigChoice, ratio=0.50, index=5, mul=bass_amp, add=0).mix(2)
bass_filter = MoogLP(bass_instru, 300, res=.2*fil_lfo, mul=.65*globamp, add=0).out()

## Melo
melo_notes = {"octOne":[84, 88, 91], "octTwo":[86,89,93], "octThr":[83,86,89]}
melo_env = ExpTable([ ( 0 , 0 ) , (1000 ,1) , (1200 ,1) , (4000 ,.5) , (8100 ,0) ] , size =8192)
melo_beat = Beat(time=noteSpeed["oneOne"], taps=8, w1=50, w2=60, w3=0, poly=1, onlyonce=False).play(delay=noteSpeed["twoOne"]*6)
melo_chordChange = TrigFunc(melo_beat['end'], chords)
melo_trigChoice = TrigChoice(melo_beat, choice=[midiToHz(x) for x  in melo_notes["octOne"]], port=0.005)
melo_amp = TrigEnv(melo_beat, table=melo_env, dur=noteSpeed["oneOne"], mul=.5)

melo_instru = FM(carrier=melo_trigChoice, ratio=0.50, index=5, mul=melo_amp, add=0).mix(2)
melo_filter = MoogLP(melo_instru, freq=800, res=.75, mul=1, add=0)
melo_delay = SmoothDelay(melo_filter, delay=0.25, feedback=.31, crossfade=0.05, maxdelay=1, mul=1, add=0)
melo_rev = Freeverb(melo_delay, size=.9, damp=0.50, bal=0.7, mul=.5*globamp, add=0).out()

## Noise
noise_amp = Fader(fadein=.01, fadeout=3.99, dur=4, mul=0.1, add=0).play(delay=noteSpeed["twoOne"]*6)
noise = Noise(mul=noise_amp, add=0).mix(2)
noise_verb = Freeverb(noise, size=1, damp=0.50, bal=1, mul=1, add=0)
noise_filter = MoogLP(noise_verb, freq=3000, res=0, mul=.25, add=0).out()



s.gui(locals())