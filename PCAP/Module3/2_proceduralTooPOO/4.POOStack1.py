""" Procedural to POO """

# Creation of the Stack class
class Stack:
    # creation of a special function calls "constructor"
    def __init__(self):
        # creation of a property that all the instancies of this class will have
        self.stack_list = []
        # if you want to make this property protected add __ double underscore before the name of the property
        self.__stack_list_protected = []

# creation of the object
stack1 = Stack()
print(len(stack1.stack_list))

# you can't access to a protected attribute from outside a class
try:
    print(stack1.__stack_list_protected)
except AttributeError:
    print('It looks like this attribute doesn\'t exist or it\'s protected')

''' Note: The constructor function is responsible to add all the 
attributes/properties specified inside itself, to all objects that
will be created, and the parameter "self" represents the object
reciently created, so when a new object is created, implicitly the
constructor is called in order to give all the instructions to the
object about how it's going to be created'''

''' "self" parameter is used to manipulate and improve the object,
it is not neccesary to call it that but it is a good practice'''

''' to create a new property/attribute you must follow the
punctuation rule; this is its syntax:
self.nameOfTheProperty = literalOrStructureData and to access this
property from outside the class you must follow the same rule
unless that property is protected, this concept is called
"encapsulation" '''