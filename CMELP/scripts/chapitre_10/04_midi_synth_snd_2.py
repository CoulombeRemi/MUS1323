from pyo import *

class SndSynth:
    def __init__(self, path, first=0, last=127):
        self.table = SndTable(path)
        self.notein = Notein(poly=10, scale=2, first=first, last=last)
        # Duree de lecture de la table = duree_table / facteur_transpo
        self.dur = self.table.getDur() / self.notein['pitch']
        self.amp = Port(self.notein['velocity'], risetime=0.001, mul=.5)

        # Notein["trigon"] envoie un trig sur reception d'un noteon.
        self.snd = TrigEnv(self.notein["trigon"], table=self.table,
                           dur=self.dur, mul=self.amp).mix(1)
        self.mix = self.snd.mix(2)

    def out(self):
        self.mix.out()
        return self

    def sig(self):
        return self.mix

# Affiche la liste des interfaces midi
pm_list_devices()

# Remplacer la valeur en idev par l'interface desiree
idev = pm_get_default_input()

s = Server()
s.setMidiInputDevice(99)
s.boot()

# Clavier Midi separe en regions par octave entre les DOs
li = []
for i in range(1, 7):
    filename = 'snd_%i.aif' % i
    firstkey = i * 12 + 24
    li.append(SndSynth(filename, first=firstkey, last=firstkey+11).out())

s.gui(locals())
