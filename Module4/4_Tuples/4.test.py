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

'''7.If you want to create a tuple with only one element, after it, must to put a comma'''
t=(1,)
print(type(t))

'''8.Also you can create a tuple of this way'''
t2 = tuple()
print(t2)

'''9.You can create the other data types with this sintax too'''
s=str()
print(s)

'''Or either here too'''
l=list()
print(l)
l1:list #Declaring a variable
l1=1,2,3 #Initializing a variable
print(l1)

'''But even if you declare a variable, but you initialing that variable with another type
of data, the variable will belong to data type that previously you assigned it'''
t3:tuple
t3=1 #you need to add a comma at the end of "1"
print(t3)
print(type(t3))
