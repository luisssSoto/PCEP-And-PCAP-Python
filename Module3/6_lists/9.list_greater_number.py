
print("The greater number")
l1=[17,3,5,80,45,100,]
greater=l1[0]
for i in l1[1:]:
    if i > greater:
        greater = i
print("The list's greater number is:", greater)


#Note: All the changes in situ, will be executed in the list, but if there is
#a change not in situ, the changes only will be in the list where you did the change
print('del and slices')
l1=['l','u','i','s']
l2=l1
l3=l2
del l2
print(l1)