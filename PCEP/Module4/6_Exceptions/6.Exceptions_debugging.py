'''Debugging'''
'''The tool usually used to inspect a code is called Debug and
the proccess to do this tool is called debugging'''
'''On the example below, there is a three paths that you Python's
interpret could pass, there is an intentional bug on the line
12, but Python can run well due of python is an interpreter language'''

user_number=0
if user_number>0:
    print(f'your number {user_number} is greater than 0')
elif user_number<0:
    prin(f'your number {user_number} is less than 0')
else:
    print(f'your number {user_number} is 0')

'''There are two sort of debugging'''
'''1. Interactive Debugging
   2. Printing Debugging'''

'''Remind that there is another technique to test your code
but there is more complex which calls Unit Test, this test
needs its own environmet to run the tests automatically'''
