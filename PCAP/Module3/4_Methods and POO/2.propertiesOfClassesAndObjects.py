""" Some intereting Properties/Attributes of Classes and Objects """
'''1. __dict__ 
Class: shows us methods; (constructor) variables of class
Object: shows us variables of instance'''
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2
    def method(self):
        pass
    def __hidden(self):
        pass

obj = Classy()
obj.method() # even wheter we call the method from the object, the __dict__ attribute doesn't recognize it
print(obj.__dict__)
print(Classy.__dict__)
print()

'''2. __name__ for Classes and type() for the objects
Note type() returns a class so that, once the class get returned
we can call __name__ attribute otherwise is not allow to use __name__
directly in the object'''
class ClassyB:
    pass

print(ClassyB.__name__)
objB = ClassyB()

try:
    print(objB.__name__)
except AttributeError:
    print(type(objB).__name__)
print()
    
'''3. __module__ says us the module that belongs that class, but, remember if the answer
of it is __main__ it means that this file is executing in that specific momement'''

class ClassyC:
    def __init__(self):
        pass

objC = ClassyC()
print(objC.__module__)
print(ClassyC.__module__)
print()

'''4. __bases__ only works in Classess like __name__ and it is tuple that shows us
the classes that one class belongs, if there is any superclass explicit of a class the 
result will be "object" which is like a superclass of Python which is predefined, that function
returns the class like type() so if you want to print a better format you can use __name__'''

class SuperOne:
    pass
class SuperTwo:
    pass
class Sub(SuperOne, SuperTwo):
    pass

def printBases(oneClass):
    print('(', end=' ')
    for cls in oneClass.__bases__:
        print(cls.__name__, end=' ')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

print(SuperOne.__bases__)
print(Sub.__bases__)







