###########################################################################
# --- Ecriture et lecture de fichier sur le disque dur. ---               # 
# 1 - Generation de 4 melodies de 16 notes chacune dans un fichier.       #
# 2 - Relecture du fichier et conversion des lignes en liste d'entiers.   #
# 3 - Petit algo qui boucle sur les listes de notes et controle un synth. #
###########################################################################
from pyo import *
import random

s = Server().boot()

# Do mineur harmonique (on pige les notes dans cette liste a l'aide d'un index).
scale = [36,38,39,41,43,44,47,48,50,51,53,55,56,59,60,62,63,65,67,68,71,72]
# Reference a la longueur de la liste-1 parce que randint inclut le maximum.
maxn = len(scale) - 1
# Index de depart pour la generation des melodies.
index = random.randint(0, maxn)

# Fonction de marche aleatoire (retourne +/- 3 par rapport a l'index precedent).
def drunk():
    # On veut modifier la variable global "index", et non en creer une locale.
    global index
    # On additionne a "index" un entier pige au hasard entre -3 et 3.
    index += random.randint(-3,3)
    # Assure que index reste toujours entre 0 et maxn (longueur de la liste).
    if index < 0:
        index = abs(index)
    elif index > maxn:
        index = maxn - (index - maxn)

### Ecriture d'un fichier texte ###

# Ouvre un fichier en mode ecriture.
f = open("notes.txt", "w")
# Genere 4 lignes de 16 valeurs.
for i in range(4):
    for j in range(16):
        # Change la variable globale "index".
        drunk()
        # Ecrit le nouvel index, suivi d'un espace, dans le fichier.
        f.write(str(index) + " ")
    # Apres chaque groupe de 16 valeurs, on change de ligne.
    f.write("\n")

# Ferme le fichier
f.close()

### Lecture d'un fichier texte ###

# Ouvre le fichier en mode lecture et recupere les melodies.
f = open("notes.txt", "r")
# Chaque ligne est un element (un string contenant 16 chiffres) d'une liste.
mel_list = f.readlines()
# On ferme le fichier.
f.close()

### Conversion d'une chaine de caracteres en liste d'entiers ###

# On enleve les retours de chariot.
mel_list = [l.replace("\n", "") for l in mel_list]
# On separe les donnees dans chaque liste.
mel_list = [l.split() for l in mel_list]
# On convertit chacun des strings en entier.
for i in range(4):
    for j in range(16):
        mel_list[i][j] = int(mel_list[i][j])

# Ici, mel_list contient 4 listes de 16 index pour lire dans la liste "scale".

############# Processus audio (synth old school) ###############

# Enveloppe d'amplitude
f = Fader(fadein=.005, fadeout=.05, dur=.125, mul=.1)
# 10 frequences bidons (pour initialiser un chorus)
freqs = [100]*10
# 10 ondes carrees.
a = LFO(freq=freqs, sharp=.75, type=2, mul=f)
# synth -> disto -> reverb
pha = Disto(a.mix(2), drive=.85, slope=.95, mul=.2)
rev = WGVerb(pha, feedback=.75, cutoff=3000, bal=.2).out()

############# Section controles ###############

# Variables globales...
mel = 0 # Laquelle des 4 melodies.
count = 0 # Compte des temps dans la melodie.
def new_note():
    global mel, count
    # Recupere l'index courant (dans la melodie "mel", au temps "count".
    ind = mel_list[mel][count]
    # Recupere la note midi dans la liste "scale".
    midi = scale[ind]
    # Calcul de la frequence en Hertz.
    freq = midiToHz(midi)
    # Chorus de 10 valeurs autour de la frequence pigee.
    freqs = [freq*random.uniform(.99,1.01) for i in range(10)]
    # Amplitude plus grande aux 4 temps (accent sur les temps forts).
    if (count % 4) == 0:
        f.mul = .1
    else:
        f.mul = .03
    # Incremente le compte (pour avancer au prochain appel de la fonction).
    count += 1
    # Actions a la fin de la mesure:
    if count == 16:
        # Remettre le compte a 0.
        count = 0
        # 50% du temps on pige une nouvelle melodie.
        if random.randint(0,1) == 0:
            mel = random.randint(0,3)
            print("nouvelle liste d'index :", mel)
    # Assigne les frequences aux oscillateurs et demarre l'enveloppe.
    a.freq = freqs
    f.play()

# Appelle "new_note" 8 fois par seconde.
pat = Pattern(time=.125, function=new_note).play()

s.gui(locals())