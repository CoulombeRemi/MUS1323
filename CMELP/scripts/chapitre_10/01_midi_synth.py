from pyo import *

class Synth:
    def __init__(self, transpo=1):
        # Facteur de transposition
        self.transpo = Sig(transpo)
        # Recoit les notes Midi et les assignes sur 10 voix de polyphonie
        self.note = Notein(poly=10, scale=1, first=0, last=127)
        # Traitement des valeurs de hauteur et d'amplitude des notes Midi
        self.pit = self.note['pitch'] * self.transpo
        self.amp = MidiAdsr(self.note['velocity'], attack=0.001, 
                            decay=.1, sustain=.7, release=2, mul=.1)
        # Chorus de 4 oscillateurs, mixes en mono pour eviter
        # l'alternance panoramique des 10 voix de polyphonie
        self.osc1 = SineLoop(self.pit, feedback=0.12, mul=self.amp).mix(1)
        self.osc2 = SineLoop(self.pit*.997, feedback=0.12, mul=self.amp).mix(1)
        self.osc3 = SineLoop(self.pit*.994, feedback=0.12, mul=self.amp).mix(1)
        self.osc4 = SineLoop(self.pit*1.002, feedback=0.12, mul=self.amp).mix(1)
        # Mixage stereo
        self.mix = (self.osc1+self.osc2+self.osc3+self.osc4).mix(2)

    def out(self):
        "Active l'envoi du signal aux sorties et retourne l'objet lui-meme."
        self.mix.out()
        return self

    def sig(self):
        "Retourne l'objet qui produit le signal final de la chaine audio."
        return self.mix

# Configuration audio/midi
idev = pm_get_default_input()
s = Server()
s.setMidiInputDevice(idev) # Changer idev en fonction de votre configuration
s.boot()

a1, a2 = Synth(), Synth(.5) # octave reel et octave inferieur

# La Somme des signaux des synths passe dans une reverberation
rev = WGVerb(a1.sig()+a2.sig(), feedback=.8, cutoff=3500, bal=.3).out()

s.gui(locals())
        
