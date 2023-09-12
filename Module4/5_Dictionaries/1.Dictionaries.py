"""Dictionaries"""
dict1={1:'one',2:'two',3:'three'}
print(dict1)

'''Iteration'''
for i in dict1:
    print(i,":",dict1[i])

'''len() function'''
print(len(dict1))

'''Get value throught keyword'''
print(dict1[3])

'''in and not in'''
test=(1,2,3,4,5)
for i in test:
    if i in dict1:
        print(i, "keyword exist in the dictionary", i, ":", dict1[i])
    else:
        print('The element', i, "doesn't exist")

'''Note: Remember all types the data can be a key, but there is an 
exception with a list, set and dictionary'''

'''List as a key'''
list2=[1,2]
dict2={}
try:
    dict2={list2:'list'}
except TypeError:
    print('TypeError, you can\'t assign a list type as key')

'''Set as a key'''
set1={'set1', 1, True}
try:
    dict2={set1:'set1'}
except TypeError:
    print('TypeError, you can\'t assign a set type as key')

'''Dict as a key'''
dict0={'dictionary':0}
try:
    dict2={dict0:'dictionary 0'}
except TypeError:
    print('TypeError, you can\'t assign a dictionary type as key')
    
'''Tuple as a key'''
tuple1=(1,2)
try:
    dict2 = {tuple1:'tuple'}
    print('It\'s possible to assign a tuple as a key')
except TypeError:
    print('TypeError, you can\'t assign a tuple type as key')
print(f'The value of the: {dict2.keys()}, is: {dict2.values()}')

'''Boolean as a key'''
try:
    dict2={True:'Verdad', False:'Mentira', True:'Otra verdad'}
    print('It\'s possible to assign a Boolean as a key')
except TypeError:
    print('TypeError, you can\'t assign a boolean type as key')

'''Note: But remember that you can only assign an unique key,
to avoid problems with the keys'''
print(dict2[True])
print(dict2.keys())

dict3={1:'one', 2:'two', 1:'uno'}
print(dict3[1])
