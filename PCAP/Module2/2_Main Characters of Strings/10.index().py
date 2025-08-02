''' .index() method'''
string = "aeiou"
list_vowels = ['a', 'e', 'i', 'o', 'u']
print(string.index('e'))
print(list_vowels.index('a'))

# Note: the same case for min and max functions, about the ValueError
try:
    list_vowels.index('z')
except ValueError:
    print("The element doesn't exist")
