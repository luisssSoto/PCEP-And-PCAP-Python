tuple1=1,2,3,
tuple2=1.0,.2,3.,
print(tuple1)
print(tuple2)

'''1. You can add each other: +'''
tuple2+=tuple1
print(tuple2)

'''2. Also multiply them'''
tuple1*=3
print(tuple1)

'''3. You can unpack the tuple too'''
zoo = ('tiger', 'mono')
danger, funny = zoo
print(danger, funny)

'''4. not in and in are allowed in tuples too'''

print('lion' in zoo)
print('mono' not in zoo)

'''5. remember the method count'''
print(tuple1.count(1))

'''6. you can read any data of the tuple and know its length'''
for animal in zoo:
    print(f'animal {animal}')

print(len(zoo))