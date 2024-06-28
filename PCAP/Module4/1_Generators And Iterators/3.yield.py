"""yield """
'''You can use an efficient and elegant approach instead the iterator protocol,
instead to save the state of the iteration from __iter__ you can use the keyword
yield instead the keyword "return"'''

def f(n):
    for i in range(n):
        return i

print(f(10))
    
'''The function above can't be a generator and alse because can't save and 
restore its state in the future, but yield does'''
def f(n):
    for i in range(n):
        yield i

'''This function now won't show the element that we are looking forward, if we
try to call it, it will show us the id of the object, because this funcition now,
is a generator object not a function'''

print(f(10))

'''Remember the ways you can access to a generator object'''
'''1.'''
for i in f(10):
    print(i)

'''2.'''   
f1 = f(5)
for i in f1:
    print(i, end=' ')
