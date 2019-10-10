a = [4,5,6,3,4,5,6,9,1,2]
b = []

for i in range(10):
    if a[i] < 5:
        b.append(a[i]**2)
    
print(b, end=" ")


b = [val**2 for val in a if val < 5]
print(b)

