"""Your own hierarcy of Exceptions"""
'''You can create a hierarcy of Exceptions that become from
the Exceptions which already exist from Python or create new ones
completely news'''

'''1. Exceptions that belongs to an specific Exception'''

class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_division(is_mine):
    if is_mine:
        raise MyZeroDivisionError('worst news')
    else:
        raise ZeroDivisionError('bad news')
    
for mode in [False, True]:
    try:
        do_division(mode)
    except ZeroDivisionError as e:
        print('original division', end=" : ")
        print(e.args)

for mode in (False, True):
    try:
        do_division(mode)
    except MyZeroDivisionError as e:
        print('my own division exception', e)
    except ZeroDivisionError as e:
        print('division original again', e)
        
