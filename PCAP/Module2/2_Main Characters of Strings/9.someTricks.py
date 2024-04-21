""" some methods and functions for Strings and Lists"""

'''min() function accepts a string as parameter '''
string = 'eEIiaA'
print(min(string))

listVowels = ['a', 'A']
print(min(listVowels))

'''max() available for Strings and lists'''
print(max(string))

print(max(listVowels))

#Note: both functios will be an error if you try to access an non-existent element
try:
    print(max(''))
except ValueError:
    print("It's a value error because there is nothing inside the variable")

''' .index() method'''

print(string.index('E'))
print(listVowels.index('a'))

# Note: the same case for min and max functions, about the ValueErrorf
try:
    listVowels.index('z')
except ValueError:
    print("The element doesn't exist")

''' list() function '''
string3 = '1234'
listString3 = list(string3)
print(listString3)

#Note: list() function works whit more literals not only with strings
tuple1 = (1, 'a', True)
print(list(tuple1)) 

''' .count() method'''
serpientSays = 'sss'
print(serpientSays.count('s'))
print(serpientSays.count('ss'))

#Note: even though if the argument given is not in the string, there won't be any error
print(serpientSays.count('t'))
