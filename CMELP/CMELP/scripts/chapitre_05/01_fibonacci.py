seuil = 100
a = b = 1
while b < seuil:
    print(b, end=" ")
    a, b = b, a+b
print()
