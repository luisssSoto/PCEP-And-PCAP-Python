'''Be careful because you can overwrite the entities of one namespace,
if you use a "selective import"'''

from math import e
#user of module
print(e)

#provider of module
e = 'elephant'
print(e)

#Note if you try to do it but in reverse the change is the same the most
#recent definitions overwriten the old ones

pi = 'piPiPI!'
print(pi)

from math import pi
print(pi)