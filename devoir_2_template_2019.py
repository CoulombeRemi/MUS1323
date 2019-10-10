"""
Création d'un instrument de synthèse et lecture d'une mélodie aléatoire.

Création de l'instrument de synthèse
------------------------------------

Votre instrument doit générer un signal stéréo et être entièrement construit à 
partir de source de synthèse (pas de lecture de fichiers sons). On doit y retrouver:

    - Au moins une source de synthèse de votre choix.
    - Une enveloppe d'amplitude d'une durée de 100 millisecondes modulant le gain de la source.
    - Au moins un paramètre de la source automatisé à l'aide d'un signal audio (de type random ou lfo).
    - La source doit passer dans un délai de 1 seconde (on veut entendre l'original ET le signal délayé).
    - On conclut en acheminant la somme des signaux dans une réverbération.

Génération mélodique aléatoire
------------------------------

- Déterminez d'abord une liste de hauteurs possibles, spécifiées en notes MIDI puis 
  transposées en Hertz, parmi lesquelles votre générateur de mélodie pourra piger.
- Créez une fonction python et faîtes-en sorte quèlle soit appelée automatiquement à toutes les 125 ms.
- À chaque appel, la fonction doit: 
    - Choisir une fréquence au hasard dans la liste des hauteurs possibles et 
      l'assigner à l'instrument créé dans la section précédente.
    - Marquer les temps forts, c'est à dire que l'amplitude de la première note de 
      chaque groupe de 4, doit être plus élevée que les autres. 
      (| = temps forts, . = temps faibles)
      | . . . | . . . | . . . | . . . etc.
    - Activer l'enveloppe d'amplitude de l'instrument pour faire jouer la note.

"""
from pyo import *
import random

s = Server().boot()





s.gui(locals())
