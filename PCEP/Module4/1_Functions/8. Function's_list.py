"""Function's list """
print("Welcome functions(list)")

"""List as Parameter"""
def listAsParameter(list1):
    sum=0
    for i in list1:
        sum+=i
    return sum

print(listAsParameter([2,3,2]))

"""Returning a List"""
def returnList(number1):
    list3=[]
    for i in range(number1):
        list3.append(i)
    return list3

print(returnList(5))
