"""Try-except and the "args" property"""
'''This property belongs to "BaseException" and show us a tuple 
of the parameters which were pass to the constructor of the 
class (Exception)'''

def print_args(args):
    length = len(args)
    if length == 0:
        print('')
    elif length == 1:
        print(args[0])
    else:
        print(str(args))

try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print_args(e.args)
try:
    raise BaseException('my exception')
except BaseException as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print_args(e.args)    
try:
    raise KeyError('my', 'dictionary error')
except Exception as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print_args(e.args)        


'''Trying with the ZeroDivisionError'''
try:
    n = 2 / 0
except ZeroDivisionError as e:
    print(e, e.__str__(), sep=" : ", end=" : ")
    print(e.args)