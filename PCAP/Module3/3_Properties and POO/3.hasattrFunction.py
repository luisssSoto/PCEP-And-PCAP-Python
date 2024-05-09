""" Checking if the class/object has an attribute/object """

'''Remember that different objects which belong to the same class could be different
attributes: '''

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = val
        else:
            self.b = val
            
example_object = ExampleClass(1)

print(example_object.a)
# print(example_object.b) # --> if uncomment it this line an AttributeException will get launched
print()

''' you can add a try-except clause, but it's not the best solution'''
try:
    print(example_object.a)
    print(example_object.b)
except AttributeError:
    pass

''' so, there is a best solution to handle these cases, for example with the hasattr()
function, its sintax is the next one:
hasattr(nameOfClass/Object 'nameOfAttribute/Property')
look how we can solve the last problem: '''

if hasattr(example_object, 'b'):
    print(example_object.b)
print()
    
''' Here is another example with a class'''
class ExampleClassB:
    attr = 0

print(hasattr(ExampleClassB, 'attr'))
print(hasattr(ExampleClassB, 'attribute'))
print()

''' Look if there is a strange behavior of this below '''
class ExampleClassC:
    a = 1
    def __init__(self):
        self.b = 2
        
example_objectC = ExampleClassC()

print(hasattr(example_objectC, 'a'))
print(hasattr(example_objectC, 'b')) 
print(hasattr(ExampleClassC, 'a')) 
print(hasattr(ExampleClassC, 'b')) 

''' But be careful when you use this function 'cause as you can note, although the behavior
of the class is expect, the object is different, eventhough the object doesn't have an 
attribute "a" (because this is a variable of class) the functions says the opposite '''