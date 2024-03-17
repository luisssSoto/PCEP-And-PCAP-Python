"""Mutable List"""
print("Welcome to Mutable List")
l1=[1]
l2=[]
l2=l1
l1[0]="one"
print(l1)
print(l2)
print("It's a little bit of weird rigth?")

'''The characteristic most important of the list is its mutability so all the 
changes that you do in them in situ will be reflect in the same list, and this 
behavior is because all the list that you create will be in only one memory's 
direction, even if you assign one list to another one will have the same memory's 
direction'''

body=['head','eyes','nose']
print(body)
print(id(body))
human=body
print(human)
print(id(human))
human.insert(-1,'mouth')
print(body)
print(human)
print()

"""but remember all the changes will be reflected to the other list when the changes
were in situ"""
female=human
female.append('beatiful')
print(body,human,female,sep='\t')
del female
print(body)
print(human)
try:
    print(female)
except NameError:
    print('The list doesn\'t exist')
    
'''The program ran and couldn\'t find the list because the "del" instruction deleted
only the list "female" and not the others list'''
print()
'''Note: all the literals except list,dictionary and sets are mutables, the other literals
are inmutables and this is because you can't change these literals in situ'''
literal1=5
print(literal1)
print(id(literal1))
literal2=literal1
print(literal2)
print(id(literal2))
literal2-=2
print(literal1)
print(id(literal1))
print(literal2)
print(id(literal2))
