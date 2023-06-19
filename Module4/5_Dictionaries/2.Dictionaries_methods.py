"""Dictionaries -methods"""
print("'Welcome dictionaries' methods")

'''Iterating'''
dictSpanishEnglish={'gato':'cat', 'dinosaurio':'dinosaur', 'rinoceronte':'rhino'}
for i in dictSpanishEnglish:
    print(i,"--->",dictSpanishEnglish[i])
print()

'''.keys method'''
print('keys method')
print(dictSpanishEnglish.keys())

for key in dictSpanishEnglish.keys():
    print(key,"--->", dictSpanishEnglish[key])
print()

'''sorted() dict'''
print('sorted function:')
for key in sorted(dictSpanishEnglish.keys()):
    print(key,"--->",dictSpanishEnglish[key])
print()

'''.items()'''
print('items method:')
print(dictSpanishEnglish.items())
for esp,eng in dictSpanishEnglish.items():
    print(esp,eng)
print()

'''.values()'''
print('values method:')
print(dictSpanishEnglish.values())
for i in dictSpanishEnglish.values():
    print(i)