"""assert keyword"""

'''1. It is used to be completely sure the integrity of the data, it's like to be
more safety about the invalid data, you can do it when you don't have the whole
information about a package, module or user's function will return to you'''

def knowingIMC(weight, height = 1.80):
    assert weight > 10
    return (weight / (height ** 2))

# print(knowingIMC(4)) # Play with the values to see the AssertionError

# Note: the AssertionError always will be launched, when exist a 0, None and False
# as a result

'''2. it's possible not only evaluate a condition but you can do this'''
# Note: change the line 11 in comments to run the next code

def behaviorAssert(value):
    print(value)
    assert value

try:
    behaviorAssert(False) # Note: change the value in (0, None, or False)
except AssertionError:
    print('you can handle the Assertion Error')
