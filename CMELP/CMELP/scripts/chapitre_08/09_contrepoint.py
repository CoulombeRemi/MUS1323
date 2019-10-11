#!/usr/bin/env python
# encoding: utf-8
from pyo import *
import random

s = Server().boot()

TIME = .2 # Duree d'un tap
# Dictionnaire de modes pour le choix des notes
SCLS = { 'p1': [0,2,5,7,9], 'p2': [0,3,5,7,10], 'p3': [0,2,7,8,11] }

# Envelope d'amplitude
env = LinTable([(0,0), (300,1), (1000,.7), (6000,.7), (8191,0)], size=8192)

# 8 randis a multiplier aux notes pour creer un chorus
cho = Randi(min=.99, max=1.01, freq=[random.uniform(1,3) for i in range(8)])

met = Beat(time=TIME, taps=16, w1=70, w2=70, w3=50).play()
amp = TrigEnv(met, table=env, dur=met['dur'], mul=met['amp'])
fr = TrigXnoiseMidi(met, dist=12, x1=1, x2=.33, scale=0, mrange=(48,85))
frsnap = Snap(fr, choice=SCLS["p1"], scale=1)
osc = LFO(freq=frsnap*cho, sharp=.75, type=3, mul=amp*0.1).mix(2)

met2 = Beat(time=TIME, taps=16, w1=100, w2=40, w3=20).play()
amp2 = TrigEnv(met2, table=env, dur=met2['dur'], mul=met2['amp'])
fr2 = TrigXnoiseMidi(met2, dist=12, x1=1, x2=.5, scale=0, mrange=(36,61))
frsnap2 = Snap(fr2, choice=SCLS["p1"], scale=1)
osc2 = LFO(freq=frsnap2*cho, sharp=.75, type=3, mul=amp2*0.1).mix(2)

rev = WGVerb(osc+osc2, feedback=.7, cutoff=4000, bal=.15).out()

def newbeat(): # Genere de nouvelles sequences rythmiques
    met.new()
    met2.new()

def change(): # actions a la fin de chaque mesure
    print('fin de la mesure')
    if (random.randint(0,100) < 25): # 25% de chance de piger une nouvelle gamme
        gamme = random.choice(['p1', 'p2', 'p3'])
        frsnap.choice = SCLS[gamme]
        frsnap2.choice = SCLS[gamme]
        print("Nouvelle gamme :", gamme)
    if (random.randint(0,100) < 20): # 20% de chance de piger un nouveau rythme
        print("Change de rythme")
        newbeat()

# Appelle la fonction change a chaque fin de mesure
ch = TrigFunc(met['end'], change)

s.gui(locals())