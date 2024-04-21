'''import packages'''
'''As the same way like modules we can import them with
path list belongs to module sys, but the packages need
initialization, this initialization is creating a file .py
calls "__init__py" which must be in the main package and
the other packages if they need different initialization'''
from sys import path
path.append('..\\packages')

'''you can import them whatever way you want'''
# import extra.iota
# print(extra.iota.FunI())

from extra.iota import FunI
print(FunI())

'''Now we can import the sigma and tau functions'''
import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

'''You can use aliasing as well'''
import extra.good.alpha as al

print(al.FunA())

'''Remember that you can append a file .zip as a path'''
path.insert(0, '..\\packages\\extra.zip')

from extra.ugly.omega import FunO as funko
print(funko())