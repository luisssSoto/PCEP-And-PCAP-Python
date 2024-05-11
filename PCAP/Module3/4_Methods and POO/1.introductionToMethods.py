""" Introduction to Methods """
'''1. Declaring methods must to have 1 parameter "self" it could have more than this,
but this one can't miss, when we call it, you don't have to put it again only the arguments
after this, also the "self" parameter indicates for which object is this method'''

class Classy():
    def method(self):
        print('Method must have the parameter self as parameter')

obj = Classy()
obj.method()
print()

''' 2. Adding another parameters can be possible, but they must be after the "self",
and pass ONLY the arguments during calling of the method'''

class ClassyB():
    def method(self, par):
        print('You can add more parameters but after the "self" parameter', par)

obj1 = ClassyB()

obj1.method(1)
obj1.method(2)
obj1.method(3)
print() 

'''3. The "self" parameter helps us to the next (inside of the class):
a) Allows us to access to the instance of the class (object)
b) Allows us to access to the variable of class
c) Allows us to access to another methods'''

class ClassyC:
    varia = 2
    def method(self):
        print(self.varia, self.var)
    def other(self):
        print('Method calling another one...')
        self.method()

obj1C = ClassyC()
obj1C.var = 3
obj1C.method()
obj1C.other()
print()

'''4. __init__ the "constructor", follows the next points below:
a) must to have as a parameter "self"
b) also can have more, but when we create a new object we must to create it with
all the other parameters pass as arguments
c) initialize the intern state of the object (initialize variables of instance,
and variables of instance belong to other objects)
d) It can't return any variable 'cause it already returns the object just created
e) You can't call it from inside of the class neither from the object
f) it's a method, and a method is a function so that, it is allowed to predefine values
of its parameters'''

class ClassyD:
    def __init__(self, value = None):
        self.var = value
        
obj1D = ClassyD('The constructor')
print(obj1D.var)
obj2D = ClassyD()
print(obj2D.var)
print()

'''5. You can become a method as private'''
class ClassyE:
    def vissible(self):
        print('Vissible Method')
    def __hidden(self):
        print('Hidden Method')
        
obj1E = ClassyE()
obj1E.vissible()

try:
    obj1E.__hidden()
except AttributeError:
    print('You can\'t access to ordinary sintax to a privated method... this is the right way')
    obj1E._ClassyE__hidden()