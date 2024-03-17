'''The last way is a accept way to solve those kind of issues
but they're not the most convenient, the best way is the next
below here: '''

try:
    print('try to do this but if you couldn\'t it...')
except:
    print('try fixing it')
    
'''The last example using try_except, and we're going to get out
of the function'''
try:
    user_number=int(input("Type a number to know its square: "))
    square_number=user_number*user_number
    print(f'your number {user_number} squared is: {square_number}')
except:
    print("The data entered from the user was invalid")