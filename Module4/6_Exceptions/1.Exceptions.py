'''There are two types of errors that could happen:
1. An error inside of our own code (syntax errors)
2. An error from the user who introduce an invalid data'''
'''An example could be more helpful:'''

def square(number):
    square_number=number*number
    print(f'your number {number} squared is: {square_number}')

user_number=int(input("Type any number you want: "))
square(user_number)


'''What about if we put a string data instead an int data'''
#user_number="4"
square(user_number)

'''You can deal with this with a structural sentence'''
user_number=(input("Type any number you want: "))
if type(user_number) is int:
    square(user_number)
else:
    print("Sorry but, it seems your user_number is not an int data")


