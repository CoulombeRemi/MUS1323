f = 212

c = (f - 32) * 5. / 9

print c 

if c <= 0:
    print('Surement de la glace')
elif c >= 100:
    print("En etat d'ebulition")
else:
    print('Cette "eau" est ni trop chaude ni trop froide')
