""" POO Stack Subclasses """
''' Hierancy is a concept which means, that a subclass will have
the same properties/attributes and methods than its superclass '''

class Stack:
    def __init__(self):
        self.__stack_list = []
    def push(self, value):
        self.__stack_list.append(value)
    def pop(self):
        last_value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return last_value

# Creation a subclass of the superclass "Stack"
# syntax: class nameOfSubclass(nameOfSuperclass):
class AddingStack(Stack):
    def __init__(self):
        # here it's a good practice; put the constructor of the superclass
        Stack.__init__(self)
        # now, adding the new protected attribute of this subclass
        self.__sum = 0

''' if you don't add the constructor of its superclass any of the
properties/attributes inside of it won't be visible from any object
created of the subclass'''

'''Note: when you create any method even the constructor or when
you call them from inside the class, must have the "self" parameter
but, on the other hand when they are called from outside the class
it is not neccesary to add it'''