'''There is a way to import any entity of any module:'''
from math import e
print(e)


'''But if you select to import this way, you can not use the 
way with point notation'''
try:
    print(math.pi)
except NameError:
    print("it's not possible to do this")