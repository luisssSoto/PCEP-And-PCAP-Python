"""Exceptions Tree"""

'''The Exceptions Tree is a kind of tree where most general or abstract of the 
exceptions is on the top of the tree'''

'''1. The exception which is created will be caught for the first exception that appears,
no matter if there is a more specific exception waiting forward it a few lines above,
so that, the most abstract exceptions must be at the end of the try: except'''

# Note: this is a bad practice, but practice changing the except line in comments to see the results
try:
    print(2/0)
except BaseException:
    print('root')
except Exception:
    print('branch')
except ArithmeticError:
    print('leaves')
except ZeroDivisionError:
    print('leave 🍃')


'''2. You can choice to manage with more than one exception on the same line of the exception'''
try:
    l = [[' ', ' ', ' '] for x in range(3)]
    print(l)
    print(l[1][3])
except (IndexError, LookupError):
    print('Occurs an error related to index errors')