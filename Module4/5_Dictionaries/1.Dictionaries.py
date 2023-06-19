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