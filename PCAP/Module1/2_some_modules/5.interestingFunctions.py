"""factorial and hypotenusa"""
from math import factorial, hypot, sqrt

'''fact the second one is more precise than the first one'''
def recursivity_fact(n):
    if n == 1:
        return 1
    return recursivity_fact(n - 1) * n

print(factorial(5))
print(recursivity_fact(5))
print()

'''hypot the second one is more precise than the first one'''
opposite_leg = 3
adjacent_leg = 4
print(sqrt(pow(opposite_leg, 2) + (pow(adjacent_leg, 2))))
print(hypot(3, 4))