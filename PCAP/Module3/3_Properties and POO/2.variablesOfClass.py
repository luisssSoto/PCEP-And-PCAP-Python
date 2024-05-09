""" Variables of Class """
'''A variable of class is an attribute/property which exist in only one copy and it is 
saved without an object, In nutshills; The variable of instance can exist if there is
an object or not, but on the other hand, the variables of instance can't exist without
objects even if the variables of instance already had been initialized'''

class ExampleClass():
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)
print()

'''In conclusion:
1. the method "__dict__" won't show any variable of class, because that method only
presente the variables of instance
2. a variable of class always will show the same value in all the instances of the class
(objects) '''

class ExampleClassB:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClassB.__counter += 1

example_objectB1 = ExampleClassB()
example_objectB2 = ExampleClassB(2)
example_objectB3 = ExampleClassB(4)

print(example_objectB1.__dict__, example_objectB1._ExampleClassB__counter)
print(example_objectB2.__dict__, example_objectB2._ExampleClassB__counter)
print(example_objectB3.__dict__, example_objectB3._ExampleClassB__counter)
print()

''' If we decide to change the variable of the class as private, the way to access to it
it is the same like variable of instance'''

print(example_objectB2._ExampleClassB__counter)
print()

'''Classes also have a variable "__dict__", so we're gonna show you that the variables
of classes exist even if there is no one object'''

class ExampleClassC:
    varia = 1
    def __init__(self, val):
        ExampleClassC.varia = val # --> variable of class
        self.varia = val # --> variable of instance
        varia = val # --> variable local of the method

print(ExampleClassC.__dict__)

example_objectC1 = ExampleClassC(2)

print(ExampleClassC.__dict__)
print(example_objectC1.__dict__)

''' So as you realize the variables of class exist without any object, although when
we create an object and change the value of the variable of class by accessing to the
parameter of the constructor, the object didn't get any property/attribute because there
is any variable of instace, but, we added a variable of instance and a local variable
to look the differences between them'''




