""" Assertion Error"""
''' Tree:
BaseException <- Exception <- AssertionError'''

try:
    userName = input('Let me know your name: ')
    assert userName
    print(f'your name is: '.title(),userName)
    # asuring the string contains something inside of it
except AssertionError as e:
    print('Assertion Error: ', e)
    
# Note: AssertionError will be launched when the values are: False, 0, None and an empty string