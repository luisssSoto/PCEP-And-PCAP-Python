"""List"""
print('Welcome to the list')

numbers=[0,1,2,3,4]
print(numbers)

'''assign one element'''
numbers[0]=111
print(numbers)

'''look one element'''
print(numbers[0])

'''copy the fifth element to second element'''
numbers[1]=numbers[4]
print(numbers)

'''len() function'''
print('length of the list is:',len(numbers))
lengthNumbers=len(numbers)
print('length of the list is:', lengthNumbers)

'''del instruction'''
del numbers[0]
print('The new length of the list is: ', len(numbers))
print(numbers)

'''negative index'''
print(numbers[-1])
print(numbers[-4])

#Note It's not allow to get any index that doesn't exist
try:
    print(numbers[-5])
except IndexError:
    print('This is an IndexError')