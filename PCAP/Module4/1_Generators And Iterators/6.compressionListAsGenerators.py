"""Compression List as Generators"""
'''Both approaches have the same performance but, the second one is more elegant isn't it'''
'''1. Normal list'''
normal_list_pow_ten = []
for i in range(6):
    normal_list_pow_ten.append(10 ** i)
print(normal_list_pow_ten)

'''2. Compression List'''
compression_list_pow_ten = [10 ** i for i in range(6)]
print(compression_list_pow_ten)

'''There is a conditional expression that we can use, but there is not a common
statement conditional '''

'''1. Normal List'''
normal_10 = []
for j in range(10):
    normal_10.append(1 if j % 2 == 0 else 0)
print(normal_10)

'''2. Compression List'''
compression_10 = [1 if j % 2 == 0 else 0 for j in range(10)]
print(compression_10)

'''How to create a generator by using a compression list sintax?'''
compression_list = [k if k.isdigit() else '🚨' for k in '1s 4 d1g1t?']
generator = (l if l.isdigit() else '🚨' for l in '1s 4 d1g1t?')
print(compression_list) 
print(generator)
print()
for m in compression_list:
    print(m, end="")
print()
for n in generator:
    print(n,end="")
print()

'''It's important to remember that the generator is not a list,
so it hasn't the same entities like any other list'''
try:
    print(len(generator))
except TypeError as e:
    print(e)

'''Also it is not neccesary to save the list and the generator
insida a variable you can create them wherever you need them:'''

for element in[x for x in range(10)]:
    print(element,end='')
print()
for p in('three' if x == 3 else x for x in range(10)):
    print(p, end="")

'''IMPORTANT! although the result is the same the list was created
first and after the print() function request its element to the
list, but on the other hand the generator creates the element
one by one (every time the print() function requests the element)'''