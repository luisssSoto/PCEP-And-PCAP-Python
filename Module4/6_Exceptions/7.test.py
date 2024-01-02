"""Test of Exceptions"""

'''1. Remember the statement "try" and clausule "except"'''
try:
    print('Place to do anything without request permission')
except:
    print('Place to apologize')

'''2. Remember you can add two or more Exceptions on an clausule "except"'''
'''You even can put both of the last exceptions on the same line:'''
try:
    user_number=int(input('Type a number: '))
    result=1/user_number
    print('The reciprocal of number:', user_number,'is:', result)
except (ValueError, ZeroDivisionError, KeyboardInterrupt):
    print('''Your data is invalid, 
          you need to put only numbers 
          but omit the 0 and don't type CTRL + C''')

'''3. Don't forget to put the abstract exception to the end of "try-except"'''
try:
    user_number=int(input('Type a number: '))
    result=1/user_number
    print('The reciprocal of number:', user_number,'is:', result)
except (ValueError, ZeroDivisionError, KeyboardInterrupt):
    print('''Your data is invalid, 
          you need to put only numbers 
          but omit the 0 and don't type CTRL + C''')
except:
    print('Something more was wrong')
    
'''4. Remind the most common exceptions:
a) ValueError
b) TypeError
c) AttributeError
d) NameError
e) SyntaxError
d) KeyboardInterrupt'''