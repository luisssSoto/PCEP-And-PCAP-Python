'''Aliasing is a way to put another name to a module or to any entity'''
import math as matematicas

print(matematicas.pi)

#Note: after to do aliasing it's impossible to access to the module or
#entity with the old names
try:
    print(math.pi)
except NameError:
    print("it's not possible")

'''You can do it, but this time with an entities'''
from math import pi as PI
from math import e as E, sin as seno

print(seno(PI))