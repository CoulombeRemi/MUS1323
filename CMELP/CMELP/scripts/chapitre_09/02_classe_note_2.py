from pyo import *
import random

class Note:
    "Conteneur pour note Midi"
    def __init__(self, pit, vel):
        self.pitch = pit
        self.velocity = vel

    def getNote(self):
        "Retourne la note Midi"
        return (self.pitch, self.velocity)

    def mtof(self):
        "Retourne la frequence en Hertz de la note"
        return 8.175798 * pow(1.0594633, self.pitch)

    def vtoa(self):
        "Retourne l'amplitude de la note entre 0 et 1"
        return self.velocity / 127.

num_notes = 200
notes_list = []

pit = 64 # Initialisation de la hauteur de depart
for i in range(num_notes):
    # Marche aleatoire. Ajoute une valeur paire entre -4 et 5 au dernier pitch
    pit = random.randrange(-4, 5, 2) + pit
    # Impose des limites
    if pit < 48:
        pit = 48
    elif pit > 84:
        pit = 84
    if (i % 4) == 0:
        vel = 40 # Temps forts
    else:
        vel = random.randint(8, 25) # Temps faibles
    notes_list.append(Note(pit, vel))

s = Server().boot()

fades, oscs = [], []
for i in range(num_notes):
    note = notes_list[i]
    start = i * .125
    f = Fader(fadein=.01, fadeout=.99, dur=1, mul=note.vtoa()).play(delay=start, dur=1)
    osc = SineLoop(freq=note.mtof(), feedback=.05, mul=f).out(i%2, delay=start, dur=1)
    fades.append(f)
    oscs.append(osc)

s.gui(locals())
