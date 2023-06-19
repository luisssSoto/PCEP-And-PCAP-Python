"""Dictionaries set"""
print("Welcome to setting Dictionaries")
ages={'alex':29,'Poulette':26,'Sam':3}
print(ages)
ages['alex']=30
print(ages)

'''.update()'''
print('\n.update() method')
ages.update({'Catalyna':1})
print(ages)

'''del instruction'''
print('\ndel instruction')
del ages['Catalyna']
print(ages)

try:
    del ages['Florentino']
except KeyError:
    print('That name wasn\'t find')

'''.popitem()'''
print('\n.popitem() method')
print(ages.popitem())
print(ages)

'''.get()'''
print('\n.get() method')
print(ages.get('Poulette'))
print(ages.get(26))

'''.clear()'''
print('\n.clear() method')
ages.clear()
print(ages)

'''.copy()'''
print('\n.copy() method')
dict2=ages.copy()
print(dict2)