"""Conclusions"""
'''__str__() method'''

class Dinosaur:
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return 'Hi my name is: ' + self.__name

dinosaur1 = Dinosaur('Barney')
print(dinosaur1)
print()

'''issubclass() function'''
class Chicken(Dinosaur):
    def __init__(self, name, environment):
        # Dinosaur.__init__(self, name)
        super().__init__(name)
        self.__environment = environment
    def __str__(self):
        return 'I am a dinosaur ' + self._Dinosaur__name + ' and live in ' + self.__environment


chicken1 = Chicken('panfilo', 'farm')
print(chicken1)
print(issubclass(Chicken, Dinosaur))
print(issubclass(Chicken, Chicken))
print(issubclass(Dinosaur, Chicken))
print()

'''isinstance()'''
print(isinstance(chicken1, Chicken))
print(isinstance(chicken1, Dinosaur))
print(isinstance(dinosaur1, Chicken))
print()

'''is'''
chicken2 = chicken1
print(id(chicken1), id(chicken2), sep=' | ')
print(chicken1 is chicken2)


'''super() can access to the immediate class methods look at the 55 line'''
class God:
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        self.__mitology = 'Greg'
        return  self.__name + ' is from ' + self.__mitology + ' mitology'

class SemiGod(God):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        self.__sentence = super().__str__() + ' and it is a SemiGod'
        return self.__sentence
    
semiGod1 = SemiGod('Heron')
print(semiGod1)
print()

'''Methods are automatically hierancy from their parents'''
class Dog:
    __isPet = False
    def __init__(self, name):
        self.__name = name
        Dog.__isPet = True  
    def __str__(self):
        return self.__name + ' is a Pet? ' + str(Dog.__isPet)

class Pitbull(Dog):
    def __init__(self, name):
        Dog.__init__(self, name)

pitbull1 = Pitbull('Rocky')
print(pitbull1)
print()

'''Methods, instance or class variables could be overwritten if exist the exactly name
in any of its subclasses'''

class CaneCorso(Dog):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return 'Could be aggresive Warning ⚠️'      

caneCorso1 = CaneCorso('Chacal')
print(caneCorso1)  
        
    
        