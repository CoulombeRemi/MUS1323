from pyo import *
s = Server().boot()
a = FM(carrier=[50,74.6,101,125.5], ratio=[1.501,2.02,1.005], 
       index=[6,5,4,7,6,5,9,6,5,8,5,6], mul=.05).out()
print(len(a))
s.gui(locals())
