import random

notes = [48, 50, 52, 54, 55, 57, 59, 60, 62, 64,65, 67, 69, 71, 72]

fw = open("notes.txt", "w")

for j in range(4):
    for i in range (16):
        n = random.choice(notes)
        fw.write(str(n) + " ")
    fw.write("\n")
    
fw.close()


