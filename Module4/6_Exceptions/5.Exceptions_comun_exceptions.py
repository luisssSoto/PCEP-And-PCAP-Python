from math import sqrt as square_root

'''ZeroDivisionError'''
try:
    print(5/0)
    print(5//0)
    print(5%0)
except ZeroDivisionError:
    print('you can not do a division by zero')


'''ValueError'''
try:
    print(square_root(-100))
except ValueError:
    print('This happens when a function receives an argument of the correct data type but an inappropriate value')
    
'''TypeError'''
try:
    t=('start', 'middle', 'end')
    t[1]='half'
except TypeError:
    print('This happens when you try to apply an operation but in the wrong context')

'''AttributeError'''
try:
    l=[1,2,3]
    for element in l.key():
        print(element)
except AttributeError:
    print('This happens when you try to use a method which not exist to that type data')

'''SyntaxError'''
print('This kind of error you must avoid to manage with a try-except,\
    because it\'s better to manage them cleaning the code by ourselves')

'''NameError'''
value_float=1.1
value_int=1
value_str='1'

secret_value=value_int
secret_type=type(secret_value)

if secret_type == type(value_float):
    print(secret_value, 'is float number')
elif secret_type == type(value_int):
    try:
        prin(secret_value, 'is an int number')
    except NameError:
        print('This happens because the variable "prin" does not exist')
else:
    print(secret_value, 'is a string')