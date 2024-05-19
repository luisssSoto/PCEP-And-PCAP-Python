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
print()

''' Now probe it with variables of instance '''
class Sup:
    def __init__(self):
        self.supVar = 11

class Sub(Sup):
    def __init__(self):
        super().__init__()
        self.subVar = 12

sub3 = Sub()
print(sub3.subVar)
print(sub3.supVar)

''' In nutshillss Python searchs the properties/attributes and methods like this:
1. look inside the object
2. then, look in all the involved classes from child to Parent
3. it the two steps fail, an AttributeException will get shown '''

'''Hierarcy of Three Levels '''

class Level1:
    classVar1 = 100
    def __init__(self):
        self.instanceVar1 = 101
    def method1(self):
        return 102

class Level2(Level1):
    classVar2 = 200
    def __init__(self):
        Level1.__init__(self) # explicit approach
        self.instanceVar2 = 201
    def method2(self):
        return 203

class Level3(Level2):
    classVar3 = 300
    def __init__(self):
        super().__init__() #no explicit approach
        self.instanceVar3 = 301
    def method3(self):
        return 302

level = Level3()

print(level.classVar1, level.instanceVar1, level.method1())
print(level.classVar2, level.instanceVar2, level.method2())
print(level.classVar3, level.instanceVar3, level.method3())

'''Overriding
It means that a property/attribute or method of a SuperClass is override for
its some propertie/attribute or method of its SubClass

It is useful 'cause you can change the behavior of one method or change the
value of any variable from its SubClass'''

class Level1:
    classVar = 100
    def anyMethod(self):
        return 101

class Level2(Level1):
    classVar = 200
    def anyMethod(self):
        return 201

level = Level2()
print(level.classVar,level.anyMethod(), sep='|')