"""Calling Lambdas"""
'''The main benefit to build a lambda instead a function is that you
can call them at the same time you are building them, it's in this 
moment that the name anonym function takes more sense'''

'''1. Imagine this function'''
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=',fun(x), sep="")

def poly(x):
    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)
print()

'''2. the same function but, more elegant'''
def print_function(args, fun):
    for x in args:
        print('f(', x, ')=', fun(x), sep="")
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

'''The function poly won't be call anymore so that we can implement it
and call it at the same time'''