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

'''4. You can't access to any property/attribute or method from child class if you
use a typical approach:'''

class A:
    def __init__(self, parameter):
        self.__private_a = parameter + 1
    
a = A(1)
try:
    print(a.__private_a)
except AttributeError as e:
    print(e)

# You must to follow this approach instead
print(a._A__private_a)
print()

'''5. You can access to any variable from objects with this approach'''
class A:
    def __init__(self, v = 1):
        self.v = v
    def set(self, v):
        self.v = v
        return v
a = A(2)
print(a.set(a.v + 1),'\n')

'''6. Class Variables and Instance Variables'''
class A:
    X = 0
    def __init__(self, v = 0):
        self.Y = v
        A.X += v

a = A()
print(a.X)
b = A(1)
c = A(2)
print(a.X)
print(c.X)

'''7. hasattr(className, attributeName[string format]) function'''
class A:
    A = 'a'
    def m():
        pass

print(hasattr(A, 'A'))
print(hasattr(A, 'm'))

'''8. Be careful about how many arguments you give the object
when its been build, although __init__ constructor belongs to 
the object, we're going to get a TypeError if we don't handle 
the error'''
class A:
    def __init__(self):
        pass
try:
    a1 = A(1)
except TypeError as e:
    print(e.args)
    a1 = A()
    
print(hasattr(a1, '__init__'))
print()

'''9. any child class could replace any entity of their parent class if the name
of the entity is exactly same'''
class A:
    def __str__(self):
        return 'a'
class B(A):
    def __str__(self):
        return 'b'
class C(B):
    pass
o = C()
print(o, '\n')

'''10. issubclass() function '''
class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(C, A), '\n')

'''11. multiple inheritance depends also in what class is added first as a parameter
in the child class, try to experiment with the MRO too'''
class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(B,A):
    def c(self):
        self.a()
o = C()
o.c()
print()

'''12. another case of multiple inheritance'''
class A:
    def __str__(self):
        return 'a'
class B:
    def __str__(self):
        return 'b'
class C(A, B):
    pass
o = C()
print(o)
print()

'''13. normal inheritance, also replace any entity of their parent class'''
class A:
    v = 1
class B(A):
    v = 2
class C(B):
    pass
o = C()
print(o.v, '\n')

'''14. try-except else and finally'''
def f(x):
    try:
        x = x / x
    except:
        print('a', end='')
    else:
        print('b', end="")
    finally:
        print('c', end='')
f(1)
f(0)
print()

'''15. args property'''
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))
print()
    
'''16. Your own Exceptions, there is an interisting data on the 194 line try to
comment and uncomment to see the difference'''
class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        #self.args = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
print()
    
'''17. Generators or Iterators next topic....'''
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
for x in I():
    print(x, end="")