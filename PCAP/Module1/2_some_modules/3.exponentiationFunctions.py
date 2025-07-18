"""Exponentiation Functions"""
from math import e, exp, log, log10, log2

'''Euler number'''
print(f"Euler number: {e}")
print(f"{e} ** {3} = {exp(3)}")
print()

'''Logaritmo'''
print(log(4))
print(log(16, 2))
print(2 ** 4)
print()

'''The second function is more precise'''
print(log(10363423424255, 2))
print(log2(10363423424255))

print(log10(1000))
print()

'''Note: pow is a built-in function; you don't need to import it'''
print(pow(10, 3))