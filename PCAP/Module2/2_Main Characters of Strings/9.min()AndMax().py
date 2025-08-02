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
print()

'''min with 2 arguments'''
print(min("aAeEiI", "A"))
print(max("a", "b"))