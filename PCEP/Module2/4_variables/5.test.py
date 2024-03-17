'''Remember that the variables keep and memory's ubication
about where the literal is'''

first_ubication='hi'
print(id(first_ubication))
same_ubication=first_ubication
print(id(same_ubication))
different_ubication='bye'
print(id(different_ubication))

'''Assigning of two different ways'''
var3=3
var8=8

print('first way: ')
var8 = var8 / (2 * 3)
print(var8)

var3=3
var8=8
print('second way: ')
var8/=2*var3
print(var8)

var3+=3
print(var3)

var3-=3
print(var3)