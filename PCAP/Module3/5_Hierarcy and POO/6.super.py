""" super instruction """
''' Exist two methods to access whichever propertie/attribute, method, of one Superclass
from its Superclass'''

''' 1. Knowing the exact name of a Superclass'''
class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'My name is ' + self.name
    
class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

sub = Sub('Andy')
print(sub)
        
'''2. Unknowing the exact name of the Superclass'''

class Super:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'My name is ' + self.name
    
class Sub(Super):
    def __init__(self, name):
        super().__init__(name) # we must avoid to put "self"

sub1 = Sub('Andale')
print(sub1)
print()

'''Note: if you want to try this approach, you can't put the parameter "self" '''

'''Now trying with variables of class'''
class Sup:
    supVar = 1
    
class Sub(Sup):
    subVar = 2
    def __str__(self):
        return str(super().supVar + self.subVar)
    
sub2 = Sub()
print(sub2.subVar)
print(sub2.supVar)
print(sub2)