from pyo import *

s = Server().boot()

envHigh = LinTable([(0,0), (4096,1), (8191,0)], size=8192)

# high
met3 = Beat(time=.125, taps=16, w1=30, w2=20, w3=0, poly=8).play()
amp3 = TrigEnv(met3, table=envHigh, dur=met3['dur']*2, mul=met3['amp'])
mid3 = TrigXnoiseMidi(met3, dist=12, x1=1, x2=0.2, scale=0, mrange=(60, 84))
frsnap3 = Snap(mid3, choice=[0,2,3,5,7,8,11], scale=1)
osc3 = SineLoop(freq=frsnap3, feedback=0.05, mul=amp3*.2).mix(1)
pan3 = Pan(osc3, pan=0.3)

met2 = Beat(time=.125, taps=16, w1=30, w2=20, w3=0, poly=8).play()
amp2 = TrigEnv(met2, table=envHigh, dur=met2['dur']*2, mul=met2['amp'])
mid2 = TrigXnoiseMidi(met2, dist=12, x1=1, x2=0.2, scale=0, mrange=(60, 84))
frsnap2 = Snap(mid2, choice=[0,2,3,5,7,8,11], scale=1)
osc2 = SineLoop(freq=frsnap2, feedback=0.05, mul=amp2*.2).mix(1)
pan2 = Pan(osc2, pan=0.7)

envBass = LinTable([(0,0), (128,1), (1024, 0.5), (4096,0.5), (8191,0)], size=8192)

# bass
met = Beat(time=.125, taps=16, w1=100, w2=100, w3=[80, 80]).play()
amp = TrigEnv(met, table=envBass, dur=met['dur'], mul=met['amp'])
mid = TrigXnoiseMidi(met, dist=4, x1=10, x2=0.1, scale=0, mrange=(48, 72))
frsnap = Snap(mid, choice=[0,2,3,5,7,8,11], scale=1)
osc = SineLoop(freq=frsnap, feedback=.12, mul=amp*.4)

rev = WGVerb(pan3+pan2+osc, feedback=0.8, cutoff=4000, bal=0.2).out()

count = 0
def gogo():
    global count
    if count % 4 == 0:
        mid.x1 = 2
        met2.new()
        met3.new()
    else:
        mid.x1 = 10
    count += 1

pat = Pattern(gogo, 1).play()

s.gui(locals())