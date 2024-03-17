"""Burble Order"""
lst1=[8,10,6,2,4]
print(lst1)

isReady=True
while isReady==True:
    isReady=False
    for i in range(len(lst1)-1):
        if lst1[i]>lst1[i+1]:
            lst1[i],lst1[i+1]=lst1[i+1],lst1[i]
            isReady=True
            
print(lst1)
print()

'''another way to sort lists'''
print(".sort() method")
lst2=[8,10,6,2,4]
lst2.sort()
print(lst2)
print()

print("method .reverse()")
lst3=[8,10,6,2,4]
lst3.reverse()
print(lst3)