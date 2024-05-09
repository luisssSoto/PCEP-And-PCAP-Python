""" Properties in POO """
''' Variables of Instance '''
''' These sort of variables belong to the object, actually, its name comes from there 
(variables of instance) but not the class'''

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def set_second(self, val):
        self.second = val
        
example_object1 = ExampleClass()

example_object2 = ExampleClass(2)
example_object2.set_second(3)

example_object3 = ExampleClass(4)
example_object3.third = 5

print(example_object1.__dict__)
print(example_object2.__dict__)
print(example_object3.__dict__)

''' The code above we can say several things:
1. Diferents objects belong to the same class can have different properties/attributes
2. All the objecst by default have some methods and properties, for instance, the variable
"__dict__" which allows us to access in a safety way to all the properties/attributes that
an object has, otherwise we could launch an Exception (AttributeError)
3. Each object has its ownn properties/attributes, so that, we can't alterate the value of
the other properties by modifying only one propertie of one object
4. You can create a brand new propertie from outside of the class, and assign it to the object
no matter if the properti even doesn't exist inside of the class
5. remember that you can access to any attribute of the class from outside of it, while
that variable be public'''

'''But, what if the attributes aren't public; if they are private'''

class ExampleClassB:
    def __init__(self, val = 1):
        self.__first = val
    def set_second(self, val = 2):
        self.__second = val
        
example_object1 = ExampleClassB()

example_object2 = ExampleClassB(2)
example_object2.set_second(3)

example_object3 = ExampleClassB(4)
example_object3.__third = 5

print(example_object1.__dict__)
print(example_object2.__dict__)
print(example_object3.__dict__)

''' Here there are some additional conclusions:
1. When you add a private attribute inside a method of the class and python add
"_" + nameOfTheClass + privateAttribute, so if you call that attribute just with that
sintax it's possible to access it even if its private'''

print(example_object2._ExampleClassB__second)

''' Obviously if you add an variable of instance from outside of the class, you can
access that variable as other one 'cause it is not private'''

print(example_object3.__third)


        


