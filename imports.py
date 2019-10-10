from random import uniform, choice

# on ajoute end=("") dans le print pour que ce qui est print soit sur une meme ligne sans espaces.
# on peut ajouter des espaces entre les "" pour que les objets qui sont print soient espacé.
# mettre end="\n" fait des retoures de ligne entre les prints

i = 0
while i < 10:
    print(i, end=" ")
    i += 1

# avec le True, la boucle ne s'arrete jamais
#while True:
    print(i)
    i += 1
    
for i in ["bill", "bob", "joe"]:
    print(i, end=" ")
    
for i in range(10):
    print(i, end=" ")