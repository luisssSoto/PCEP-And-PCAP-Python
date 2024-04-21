"""Points of code and characters"""

'''getting the point of code with ord()'''
space = 5
try:
    print(ord(space))
except TypeError:
    print('the only value available as a parameter must be a string')

'''getting the character of Unicode with chr() function'''

pointOfCode = 99999999
try:
    print(chr(pointOfCode))
except TypeError:
    print('The parameter given must be an integer ')
except ValueError:
    print('The type is ok but the value inside of it is wrong')
