'''What is the greater between 2 numbers?'''
n1=int(input('Type your first number: '))
n2=int(input('Type your second number: '))

#If there is only one instruction after the condition "if"
# you can use only one line, just here:
if n1 > n2: print(n1, 'is greater than', n2)
else: print(n2,'is greater than',n1)

'''What is the greater between 3 numbers?'''
n1=int(input('Type your first number: '))
n2=int(input('Type your second number: '))
n3=int(input('Type your thirth number: '))

greaterNumber=n1
if n2 > greaterNumber: greaterNumber = n2
if n3 > greaterNumber: greaterNumber = n3
print('The greater number between',n1,n2,n3,'is:',greaterNumber)


'''You can do it easier and with l5ots of numbers'''
listNumbers=input('Type a couple of numbers separate by one space: ').split()
listIntNumbers=[int(number) for number in listNumbers]
greaterNumber=-999_999_999
for anyNumber in listIntNumbers:
    if anyNumber > greaterNumber: greaterNumber = anyNumber
print('The greater number in this list',listIntNumbers,'is:',greaterNumber)