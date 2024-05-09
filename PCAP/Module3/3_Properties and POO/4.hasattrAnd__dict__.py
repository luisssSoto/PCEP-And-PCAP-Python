""" hasattr and __dict__"""

class Python:
    population = 1
    victims = 0
    constrictor = True
    def __init__(self):
        self.length_ft = 3
        self.__venomous = False
        
python2 = Python()
print(hasattr(python2, 'constrictor'))
print(python2.__dict__)
print(python2._Python__venomous)