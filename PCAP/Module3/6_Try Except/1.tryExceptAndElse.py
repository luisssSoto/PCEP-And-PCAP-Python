"""Try except and else"""

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print('Operation failed')
        return None
    else:
        print('All it is ok')
        return n

print(reciprocal(0))
print(reciprocal(2))

'''This approach guarantes that if the block try runs,
the else block too, but on the other hand if the block
exception is executed the else block never will be execute'''