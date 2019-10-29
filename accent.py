# sert à vérifier chaque position de la liste. 
# la variable est à l'extérieur car sinon à chaque fois que la fonction est appelé (1x tous les 125ms), ca va reset et on aura jamais de résultats
trig = 0

# ca c'est une liste
# la liste à 4 choses à l'intérieur donc les positions sont : 0 - 1 - 2 - 3
# le nombre de note qui joue comprenant l'accent "1" et les 3 autres notes "0"
accent = [1,0,0,0]

def meloRan():
    global trig
    # tu vérifis que : si la valeur de la liste à la position trig (trig vaut 0, donc on regarde à la position 0 dans la liste) vaut 1, on fait quelque chose
    if accent[trig] == 1:
        # fait une accentuation avec le mul de la source
        print("+")
        
    # Sinon (si la valeur dans la liste à la position trig n'est pas 1) on fait quelque chose d'autre
    else : 
        # on laisse la valeur du mul de la source comme il est initialement ou on baisse le mul
        print("-")
        
    # apres avoir fait ces vérifications là, on veut jouer le son. donc tu fais .play() comme tu as déjà dans ton code
    fm_amp.play()
    # apres le .play(), il faut que tu incrémente la valeur de trig pour que lorsque la fonction est ré-appeler, on avant d'une position dans la liste.
    # sinon on va toujours rester à la première position dans la liste.
    # faire : trig += 1 revient à faire : trig = trig + 1
    trig += 1
    # Pour finir, tu ne veux pas que la valeur de trig dépasse la longeur de la liste. Sinon ca va juste arrêter de faire un accent.
    # Tu dois donc vérifier que SI la valeur de trig est égale (on utilise le double égale "==" pour comparer deux valeurs) à la longueur de la liste,
    # on doit remettre trig à 0 pour recommencer la lecture de la liste.
    if trig == len(accent):
        trig = 0
        
# change les noms de variables svp