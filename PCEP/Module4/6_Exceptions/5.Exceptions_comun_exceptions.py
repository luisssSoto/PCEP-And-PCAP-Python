'''There a few Exceptions that you need to know:'''

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

try:
    print(float('I wanna be a number'))
except ValueError:
    print('This is a another kind of ValueError')

'''TypeError'''
try:
    t=('start', 'middle', 'end')
    t[1]='half'
except TypeError:
    print('This happens when you try to apply an operation but in the wrong context')

try:
    d={'float': 5.5, 'int': 4, 'string': 'Python'}
    print(d.update(3,3))
except TypeError:
    print('The method was ok, but the data inside of it was wrong')

'''AttributeError'''
try:
    l=[1,2,3]
    for element in l.key():
        print(element)
except AttributeError:
    print('This happens when you try to use a method which not exist to that type data')

try:
    d={
        'carnivore': ['t-rex', 'snakes', 'tigger'],
        'hervibore': ['rhino', 'giraffe', 'cow']
        }
    d.insert(1, 'omnivore')
except AttributeError:
    print('This method doesn\'t belong to dictionaries, rather belongs to list')

'''SyntaxError'''
print('This kind of error you must avoid to manage with a try-except,\
    because it\'s better to manage them cleaning the code by ourselves')
'''These errors only you can find it when you type something like this:'''

# print('Can you see the error)


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

'''KeyboardInterrupt, try to runs the next code and type
CTRL + c on your Keyboard to see what it's a KeyboardInterrupt
Exception'''
try:
    while True:
        print('runs forever or type CTRL + c')
except KeyboardInterrupt:
    print('This is a KeyboardInterrupt exception')
print('we went get out from the code above')
