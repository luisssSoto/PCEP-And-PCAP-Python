""" Import Error """
'''Tree:
BaseException <- Exception <- StandardError <- ImportError'''

try:
    import math
    from sys import winver
    import anime
except ImportError as e:
    print('Import Error: ', e)