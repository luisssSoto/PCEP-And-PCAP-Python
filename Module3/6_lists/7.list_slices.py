"slices"
l1=['dinosaur', 'dessert', 'play']
l2=[]
l2=l1
print(l2)
l1.append('laughing')
print(l2)
del l1[0]
print(l2)
print()

l3=[]
l3=l1[:]
del l1[-1]
print(l3)
l3.insert(0,'dinosaur')
print(l3)

#Note: the last element it's not gonna be included
l4=[]
l4=l3[0:3]
print(l4)
print()

'''Negative Index'''
print("Negative Index")
l5=[1,2,3,4,5]
l6=[]
l6=l5[2:-1]
print(l6)
print()

print("In the next case the list will be empty:")
l7=l5[10:-1]
print(l7)
print()


print("[:end] - [begin-:]")
l8=[1,2,3,4,5]
l9=l8[:3]
l10=l8[2:]
print(l9, "\t", l10)
print()

print('del instruction and slices')
del l8[1:3]
print(l8)
del l8[:]
print(l8)
try:
    del l8
    print(l8)
except NameError:
    print('there is not any list to print')