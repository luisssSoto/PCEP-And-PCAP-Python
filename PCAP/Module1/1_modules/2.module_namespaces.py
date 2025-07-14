'''Namespaces'''
'''a namespace is a no phisic space where a module keeps all of its 
entities; for instance; variables, const, functions, methods, objects etc'''
'''It's possible have two entities with the same name in the same
namespace:'''
import math 

#another entity:
print(math.pi)

#my entity
pi=3.14
print(pi)

#Note: as you can see it's possible to live 2 entities in the same namespace
