from pyo import *

class Particule:
    def __init__(self, input, time=.125, q=20, 
                maxdur=.2, frange=[350,10000], poly=12):
        # Enveloppe d'amplitude
        self.table = LinTable([(0,0),(100,1),(500,.3),(8191,0)])
        # InputFader permet de faire des crossfades sur le son source
        self.input = InputFader(input)
        # Tous les parametres variables sont convertis en audio
        self.time = Sig(time)
        self.q = Sig(q)
        self.maxdur = Sig(maxdur)

        # Generation de trigs
        self.metro = Metro(self.time, poly=poly).play()
        # Pige de valeurs de frequence et de duree
        self.freq = TrigRand(self.metro, min=frange[0], max=frange[1])
        self.dur = TrigRand(self.metro, min=.01, max=self.maxdur)
        # Lecture de l'enveloppe d'amplitude
        self.amp = TrigEnv(self.metro, table=self.table, dur=self.dur)
        # Particule filtree
        self.filtre = Biquadx(self.input, freq=self.freq, q=self.q, 
                              type=2, stages=2, mul=self.amp)

    def out(self):
        "Envoie le son aux haut-parleurs et retourne l'objet lui-meme."
        self.filtre.out()
        return self

    def getOut(self):
        """ Retourne l'objet audio qui genere le signal de sortie de la 
        classe afin de pouvoir l'inclure dans une chaine de traitement."""
        return self.filtre

    def setInput(self, x, fadetime=.05):
        self.input.setInput(x, fadetime)

    def setTime(self, x):
        self.time.value = x

    def setQ(self, x):
        self.q.value = x

    def setMaxDur(self, x):
        self.maxdur.value = x