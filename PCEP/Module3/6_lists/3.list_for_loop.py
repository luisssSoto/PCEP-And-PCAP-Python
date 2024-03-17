"""For Loops and Lists"""

'''create a list with for loop'''
print("Welcome to For Loops and List")
listForAp=[]
for app in range(5):
    listForAp.append(app+1)
print(listForAp)

listForIn=[]
for ins in range(5):
    listForIn.insert(ins+1,ins+1)
print(listForIn)

'''Before we said that if you try to access to a list's index which not exist you'll
get an IndexError but when you work with .insert() method there is an exception'''
listForIn.insert(15,'it\'s allowed')
print(listForIn)


'''Indexation with for'''
numbers=[1,2,3,4,5]
sum1=0
for i in range(len(numbers)):
    sum1+=numbers[i]
print('The result of the sum is:', sum1)

sum2=0
for i in numbers:
    sum2+=i
print('The result of the sum is:', sum2)


'''Switching'''
var1=1
var2=2
print(var1, 'and', var2)

print('Traditional method')
aux=0
aux=var1
var1=var2
var2=aux
print(var1, 'and', var2)

print('Brand New Method')
var1,var2=var2,var1
print(var1, 'and', var2)

print('Now we can try this con list')
numbers[0], numbers[-1]=numbers[-1],numbers[0]
print(numbers)


'''Reverse to the list'''
num=[1,2,3,4,5,6,7,8,9,10]
print(num)
for i in range(len(num)//2):
    num[i],num[-i-1]=num[-i-1],num[i]
print(num)

#Note: There is a method for do the last, but we can see it later

'List inside to another List'
list1=[1,4,5]
list2=[2,3]
list1.insert(1,list2)
print(list1)
print(list1[1])
print(len(list1))