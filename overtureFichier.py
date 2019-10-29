f = open("notes.txt", "w")
f.write("Allo\n Tout le monde\n")
f.close()

# .read() --> li le fichier au complet
# .readline() --> li une ligne à la fois
# .readlines() --> li toutes les lignes, avec les retours de lignes
text = f.readline()
while text != "\n"
print(text)





# open("py file", "r")
# r --> read
# w --> open for writing, truncating the file first
# x --> exclusive creation
# a --> open for writing, appending to the end of the file if it exists
# t --> text mode