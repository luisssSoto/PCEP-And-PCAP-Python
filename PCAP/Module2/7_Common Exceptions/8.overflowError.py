""" Overflow Error """
''' Tree:
BaseException <- Exception <- ArithmeticiError <- OverflowError'''

import math

num = 1
condition = True

try:
    while condition:
        num = math.exp(num)
        num *= 2
        print(num)
except OverflowError as e:
    print('Overflow Error: ', e)
    # Note: there is no rason to add the code below here because it's not neccesary
    # condition = False