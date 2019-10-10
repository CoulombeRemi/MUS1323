from pyo import *
s = Server().boot()

def event_0():
    print("Appel de la fonction 0")

def event_1():
    print("Appel de la fonction 1")

def event_2():
    print("Appel de la fonction 2")

def event_3():
    print("Appel de la fonction 3")

met = Metro(time=1).play()
count = Counter(met, min=0, max=4)
score = Score(count, fname="event_")

s.gui(locals())
