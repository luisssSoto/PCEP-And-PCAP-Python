"""Functions argument's scope"""
print("Welcome argument's scope")


'''Scalar as argument'''
def f1(arg1):
    print('value of arg1:', arg1)
    arg1+=1
    print('New Value of arg1:', arg1)

arg1='one'
f1(1)
print(arg1)

'''List as argument'''
def l1(list1):
    print(list1)
    list1=[0,1]

list1=[2,3,4]
l1(list1)
print(list1)


'''List with instructions or methods'''
def l2(list2):
    print(list2)
    del list2[-1]
    list2.insert(0,-1)

list2=[2,3,4]
l2(list2)
print(list2)
