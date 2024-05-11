""" Introspection And Reflection """
''' You don't have to know the definition of the class/object, 
in order to manipulate the properties, they have metadata to allow
us to know the type and properties (introspection) and to 
manipulate the properties and methods in time of execution
(reflection) '''

'''Example'''
class MyClass:
    pass

obj = MyClass()

obj.a = 1
obj.b = 2
obj.i = 3
obj.irreal = 3.5
obj.integer = 4
obj.z = 5

def increaseIntegersI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            value = getattr(obj, name)
            if isinstance(value, int):
                setattr(obj, name, value + 1)

print(obj.__dict__)
increaseIntegersI(obj)
print(obj.__dict__)

'''Note about the functions:
1. getattr(nameOfObject, nameOfAttribute) and returns the value of that Attribute
2. isinstance(nameOfObject, SuperClassOfTheObject) and returns True or False depending which type is that object
3. seattr(nameOfObject, nameOfAttribute, newValue) and modify the value of the attribute specified
'''