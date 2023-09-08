"""Tuples"""
print("Welcome to Tuples")

'''How create a tuple'''
tuple1=()
tuple2=1,2,3,
tuple3=(4,5.3,'hi', False)
print(tuple1, "\t", tuple2, "\t", tuple3)

'''How to know the type of a variable'''
print(type(tuple1),type(tuple2),type(tuple3), sep='\t')

'''Inmutability'''
for i in tuple3:
    print(i,end='\t')

'''So that you can't do this, except the delete instruction when you
use it more abstract...'''
try:
    tuple3.insert(-1,'impossible')
except AttributeError:
    print("""\n You can't assign any methods to tuple, that make
it to change its values like list""")

try:
    tuple3[0] = 'I don\'t think so'
except:
    print('You can\'t assign any value to any tuple\'s item')

try:
    del tuple3[-1]
except TypeError:
    print('''You can\'t use del instruction to delete one 
    specific item, only you can delete all the tuple...''')
    del tuple3
    try:
        print(tuple3)
    except NameError:
        print('This is impossible because you deleted it')