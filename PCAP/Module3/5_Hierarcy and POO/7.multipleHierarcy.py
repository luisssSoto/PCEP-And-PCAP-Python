""" Multiple Hierarcy """
''' It means that a class can have more than one 
SuperClass '''

class SuperA:
    classVarA = 10
    def methodA(self):
        return 11

class SuperB:
    classVarB = 20
    def methodB(self):
        return 21

class SubC(SuperA, SuperB):
    pass

subC = SubC()
print(subC.classVarA, subC.methodA())
print(subC.classVarB, subC.methodB())


''' But we need to be careful about the overriding '''

class Left:
    classVar = 'L'
    classVarLeft = 'LL'
    def method(self):
        return 'Left'

class Right:
    classVar = 'R'
    classVarRight = 'RR'
    def method(self):
        return 'Right'

class Sub(Left, Right): #Left Class is going to be first
    pass

sub = Sub()
print(sub.classVar, sub.classVarLeft, sub.classVarRight, sub.method())

'''According with the last information we can complete our
rule regarding hierarcy '''
''' In nutshillss Python searchs the properties/attributes and methods like this:
1. look inside the object
2. then, look in all the involved classes from child to Parent
2.a but if the class is child of one more class, the class more in the left
will override the values of the other superclasses
3. it the two steps fail, an AttributeException will get shown '''