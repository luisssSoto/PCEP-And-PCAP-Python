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
        # here it's a good practice; adding the constructor of the superclass
        # Syntax: nameOfSuperclass.nameOfSuperclass'Constructor(self)
        Stack.__init__(self)
        # now, adding the new protected attribute of this subclass
        self.__sum = 0
    # then, we add the hierance the two methods of its superclass, but we add more functionanlities
    # adding the value to the protected variable __sum
    def push(self, value):
        # Syntax to call a Superclass' method: nameOfSuperclass.nameOfSuperclass'Method(self, parameters..)
        Stack.push(self, value)
        self.__sum += value
    # minus the value which is pop of the list to the __sum variable
    def pop(self):
        the_last_value = Stack.pop(self)
        self.__sum -= the_last_value
        return the_last_value
    # add another method in order to show the result of the __sum variable
    def get_sum(self):
        return self.__sum


''' if you don't add the constructor of its superclass any of the
properties/attributes inside of it won't be visible from any object
created of the subclass, in this case we're talking about the 
__stack_list'''

'''Note: when you create any method even the constructor or when
you call them from inside the class, must have the "self" parameter
but, on the other hand when they are called from outside the class
it is not neccesary to add it'''

'''When we use another method which belongs to our Superclass, and change its behavior,
this is called "cancel the method", "el metodo quedo anulado" into Spanish'''

addingStack1 = AddingStack()
for i in range(5):
    addingStack1.push(i)
    print(addingStack1.get_sum())
for i in range(5):
    print(addingStack1.pop())
print(addingStack1.get_sum())