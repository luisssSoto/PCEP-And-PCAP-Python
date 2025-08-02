"""Immutability in Strings"""

'''Any method from list in order to change the value of 
the list in situ is not available in the strings and this is
because the strings are immutables'''

string = ''
for i in range(ord('a'), ord('z') + 1):
    string += chr(i)
print(string)

'''del instruction'''
try:
    del string[0]
except TypeError:
    print('del instruction is only available, just like this: ')
    del string
    try:
        print(string)
    except NameError:
        print('this variable doesn\'t exist anymore')

string2 = ''
'''append(), insert()'''
try:
    string2.append('any')
    string2.insert(1,'something')
except AttributeError:
    print('impossible to do, because it\'s immutable')

