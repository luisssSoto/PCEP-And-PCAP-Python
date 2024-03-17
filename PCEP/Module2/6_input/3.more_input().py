'''You can type several data in one call to input() function'''
listNumbers=input('Type a few numbers separate by space:').split()
print(listNumbers)

'''If you want to print any values inside it:'''
for number in listNumbers:
    print(number,end=' ')
print()

'''But remember, that the last values are'nt really numbers (int or float)
So that you need to cast them...'''
newList=[]
for number in listNumbers:
    n1=int(number)
    newList.append(n1)

print(newList)

for number in newList:
    print(number, 'is a', type(number))