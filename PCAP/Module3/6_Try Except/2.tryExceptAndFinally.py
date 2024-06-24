"""Try Except Else and Finally"""

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print('Operation failed')
        n = None
        return None # All the returns will be ignored, and only the finally's return will appears
    else:
        print('Operation succesful')
        return n # All the returns will be ignored, and only the finally's return will appears
    finally:
        print("I always will be executed")
        return n
    
print(reciprocal(2))
print(reciprocal(0))

'''When we use finally statement whatever the result is, it is going to execute its 
code of block, also you can ommit the else and the finally element,
I mean, they can work separately too, probe it to comment the finally
and after the else block'''