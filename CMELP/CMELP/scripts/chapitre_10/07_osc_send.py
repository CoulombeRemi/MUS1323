from pyo import *

s = Server().boot()

# Un lfo qui controle la position de lecture normalisee entre 0 et 1
lfo = Sine(.1, mul=.5, add=.5)

# Controle manuel sur la transposition par grain
rnd = Sig(0)
rnd.ctrl(title="Transposition par grain")

# Envoie les controles sur le port 9000 aux destinations '/pos' et '/rand'
# host est l'adresse IP de la machine ciblee. 127.0.0.1 = machine locale
send = OscSend([lfo, Pow(rnd, 6)], port=9000, address=['/pos','/rand'], host='127.0.0.1')

s.gui(locals())