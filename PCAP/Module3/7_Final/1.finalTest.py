"""Final Test Module 3"""

'''1. LIFO meains Last-In First-Out'''

'''2.'''
class Class:
    def __init__(self):
        pass
object1 = Class()
print(object1)
print(hex(id(object1)))
print(id(object1), '\n')

'''3. You can see any method or/and attribute/property from any child class that 
belongs to its parent class even if you don't add the constructor parent to the 
constructor child, but you can't see any entity declare inside the 
constructor parent class if you don't add the constructor parent in its child
constructor:'''
class A:
    class_variable = 'class variable'
    def __init__(self):
        self.a = 1
    def any_method(self):
        self.instance_variable = 'instance variable'
        return 'any method from A'
class B(A):
    def __init__(self):
        #You can uncomment one of the next lines to see the difference
        # A.__init__(self)
        # super().__init__()
        self.b = 2
    
b1 = B()
print(b1.class_variable)
print(b1.any_method())
print(b1.instance_variable)

try:
    print(b1.a)
except AttributeError as e:
    print(e.args)