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

try:
    tuple3.insert(-1,'impossible')
    del tuple3
    tuple3[0]=0
except AttributeError:
    print("\n I'ts not possible")

