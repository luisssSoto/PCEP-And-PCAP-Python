""" __str__ method """
''' When you want show an object like a string by printing it whit the
print() function, Python look inside its class and search __str__ method,
but the most cases the result will show the memory direction where the 
object is, but, you can modify its behavior yourself '''

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

star = Star('Sun', 'Milk Way')
print(star)
print(star.__str__())
print()

''' modifying the __str__ method'''
class Star1:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return self.name + ' is in ' + self.galaxy

star1 = Star1('Sun', 'Milk Way')
print(star1)
print(star1.__str__())
print(star1.__str__) # be careful what you're trying to print
    