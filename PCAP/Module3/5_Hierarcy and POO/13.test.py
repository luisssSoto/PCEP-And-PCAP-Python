"""Final Test"""

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + ' says: ¡Guau!'

class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + ' No huyas corderito!'

class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + ' ¡Quedese donde esta, Señor Intruso!'
    
rocky = SheepDog('Collie')
luna = GuardDog('Doberman')

'''1. test'''
print(rocky)
print(luna)

'''2. test'''
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

'''3. test'''
print(luna is luna, rocky is luna)
print(luna.kennel)
print(rocky.kennel)

'''4. test
Define una subclase de SheepDog llamada LowlandDog, y equipala con un método
__str__() que anule un método heredado del mismo nombre. El nuevo método __str__() 
debe retornar la cadena "¡Guau! ¡No me gustan las montañas!".'''

class LowlandDog(SheepDog):
    def __str__(self):
        return Dog.__str__(self) + ' ¡No me gustan las montañas!'
    
cute = LowlandDog('Pastor de Valee')
print(cute)
