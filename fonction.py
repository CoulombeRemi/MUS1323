
from pyo import *
s = Server().boot()

def racine_carrees(mini, maxi, step=1):
    for i in range(mini, maxi, step):
        print("la racine carree de %d est : %f " % (i, math.sqrt(i)))
    
def power(mini, maxi, exp):
    lst = []
    for i in range(mini, maxi):
        lst.append(pow(i,exp))
    return lst
    
maliste = power(10, 15, 2)
length = len(maliste)
print(maliste)

a = Sine(freq=maliste, mul=1/len(maliste)).out()

def update(start=20, exp=2, num=length):
    lst = power(mini=start, maxi=start+num, exp=exp)
    a.freq = lst


s.gui(locals())
