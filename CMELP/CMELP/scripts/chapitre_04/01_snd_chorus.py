from pyo import *
s = Server().boot()
# Dans un path, le symbole ".." recule d'un dossier dans la hierarchie.
# Un path relatif commence au dossier ou est sauvegarde le script python.
a = SfPlayer(path="../snds/baseballmajeur_s.aif", 
             speed=[1,1.005,1.007,.992], loop=True, mul=.25).out()
s.gui(locals())
