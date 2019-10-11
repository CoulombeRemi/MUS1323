from pyo import *

class SndSynth:
    def __init__(self, path, first=0, last=127):
        # Place le son en memoire
        self.table = SndTable(path)
        # scale=2 convertit les notes midi en facteurs de transposition
        self.notein = Notein(poly=3, scale=2, first=first, last=last)
        self.transpo = self.notein['pitch'] * self.table.getRate()
        self.amp = Port(self.notein['velocity'], risetime=0.001, mul=.5)

        # Osc -> lit une table en boucle
        self.osc = Osc(self.table, freq=self.transpo, mul=self.amp).mix(1)
        self.mix = self.osc.mix(2)

    def out(self):
        self.mix.out()
        return self

    def sig(self):
        return self.mix

idev = pm_get_default_input()
s = Server()
s.setMidiInputDevice(idev)
s.boot()

# Clavier Midi separe en regions par tierce mineure
# autour des notes 60, 63, 66, 69, 72, 75
li = []
for i in range(1, 7):
    filename = 'snd_%i.aif' % i
    centralkey = 57 + i * 3
    li.append(SndSynth(filename, first=centralkey-1, last=centralkey+1).out())

s.gui(locals())
