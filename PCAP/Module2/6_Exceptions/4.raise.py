"""raise keyword"""
'''raise is used to launch the exception that you want after the keywore raise
Syntax:
raise nameOfTheException'''

'''1. first example'''
try:
    raise UnboundLocalError
except UnboundLocalError:
    print('Handling the UboundLocalError')


'''2. You can do it to evaluate the code's behavior in an expected situation'''

def launchAnException():
    raise NameError

try:
    print(launchAnException())
except NameError:
    print('Handling the exception from outside')

'''3. raise can use without the nameOfTheException but only need to be inside the
exception block, and the exception that is generated will be the same where the 
raise keyword was added'''

def launchingLastException():
    try:
        print(1/0)
    except ArithmeticError:
        print('Arithmetic Error')
        raise

try:
    launchingLastException()
except ZeroDivisionError: #also can be another more general Error
    print('Zero Division Error')