"""List Test"""
l1=[i for i in range(5)]
print(l1) #0,1,2,3,4

l2=[0 for j in range(5)]
print(l2)#0,0,0,0,0

l3=[2-k for k in range(5)]
print(l3)#2,1,0,-1,-2

l4=[3-l for l in range(-3,3)]
print(l4)#6,5,4,3,2,1

l5=[m+3 for m in range(-1,4)]
print(l5)#2,3,4,5,6

l6=[n-10 for n in range(-4,4,2)]
print(l6)#-14,-12,-10,8,

l7=[-2-l for l in range(-3,4)]
print(l7)#1,0,-1,-2,-3,-4,-5
print()

"""Changes in situ"""
list1=['a', 'b', 'c']
list2=list1
list3=list2
del list2[0]
print(list1)

"""Changes not in situ"""
del list1
print(list2)
try:
    print(list1)
except NameError:
    print('this var doesn\'t exist')

'''len in a list inside another one to another one'''
list1=[1,2]
list2=['dog', 'cat', 'mouse']
list3=['anything']

list1.insert(1,list2)
print(list1)
print(len(list1))

list1[1].insert(0,list3)
print(list1)
print(len(list1))

'''Weird cases'''
'''1. case'''
weirdList=[3, 'weird', True]
print(weirdList[weirdList[-1]])

'''2. case'''
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

'''3. case'''
'''Always when we work with slices lists though the list doesn't have
that index, it's possible to do it and there won't be any error'''
duo=[True, True, False]
choices=duo[3:]#try to delete ":"
for choice in choices[-2:]:#try to delete ":"
    if choice:
        print('*')