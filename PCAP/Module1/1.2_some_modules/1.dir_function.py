import math

print(f'Entities of {math} module: ')
print(dir(math))

#Note:
#The only condition to use dir() is the module need to be imported
#like this import nameOfModule

#We can add an alias too:
import random as ra

print(f'Entities of {ra} module: ')
print(dir(ra))