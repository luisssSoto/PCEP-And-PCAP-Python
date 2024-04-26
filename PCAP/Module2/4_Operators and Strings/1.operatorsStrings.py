"""String's Operators"""
'''It\'s possible to compare strings between them with relational
operators, but the result is surpring'''

'''1. if all characters are in the same order and the same characters
will be True'''
print('walrus' == 'walrus')
print('walrus' != 'Walrus')
print('walrus' != 'walrus!')
print()

'''2. the result of the comparation is because the point of code of 
first character is taken and it is compared between the point of
code the other first character, if both are same and the length too
soo the greater will be the long
'''
print('parakeet' < 'parakeet: hi!')
print()

'''3. remember that the lower letters are greater than upper ones'''
print('Dolphin' < 'dolphin')
print()

'''4. the same concept for the numbers, look at the point of code of
first character'''
print('10' == '010')
print('10' > '010')
print('10' > '8')
print('20' < '8')
print('20' < '80')
print()

'''5. What about if you decide to compare strings to integers, well
it'll be a bad idea, the result for "==" always will be a False
and the "!=" always will be a True, compare them with another 
relational operator will be a TypeError
'''

print('10' == 10)
print('10' != 10)
print('10' == 1)
print('10' != 1)

try:
    print('10' > 10)
except TypeError:
    print("It's a TypeError")