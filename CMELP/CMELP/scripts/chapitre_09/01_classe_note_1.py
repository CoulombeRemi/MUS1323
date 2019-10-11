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

for i in range(num_notes):
    # Pige aleatoire d'une valeur paire entre 48 et 84
    pit = random.randrange(48, 85, 2)
    vel = random.randint(10, 30)
    notes_list.append(Note(pit, vel))

s = Server().boot()

# Initialisation de listes vides pour garder les references aux objets audio
fades = []
oscs = []

### Initialisation des notes ###
# args : delay = delai avant d'activer l'objet, dur = temps d'activation de 
# l'objet (la methode stop() est appelee automatiquement)
for i in range(num_notes):
    # Recupere un objet Note
    note = notes_list[i]
    # Temps de depart de la note
    start = i * .125
    # Enveloppe d'amplitude. L'amplitude est recuperee par la methode vtoa()
    f = Fader(fadein=.01, fadeout=.99, dur=1, 
              mul=note.vtoa()).play(delay=start, dur=1)
    # Oscillateur. La frequence est recuperee par la methode mtof()
    osc = SineLoop(freq=note.mtof(), feedback=.05, 
                   mul=f).out(i%2, delay=start, dur=1)
    # Ajoute les objets dans les listes
    fades.append(f)
    oscs.append(osc)

s.gui(locals())
