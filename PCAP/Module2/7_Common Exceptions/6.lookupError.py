""" Lookup Error """
'''Tree:
BaseException <- Exception <- LookupError'''

numberTuple = (1,2,3,4)
print(numberTuple[-1])

try:
    print(numberTuple[10])
except LookupError as e:
    print('Lookup Error: ', e)