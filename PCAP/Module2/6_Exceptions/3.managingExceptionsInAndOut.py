"""Handle exceptions inside and outside functions"""
'''1. handle inside the function'''
def myFunction(n):
    try:
        print(2/n)
    except ZeroDivisionError:
        print('Handling the exception since inside')

myFunction(0)

'''2. handle outside the function'''
def myFunction2(value):
    result = 2 / value
    return result

try:
    myFunction2(0)
except ArithmeticError:
    print('Handling the exception since outside')