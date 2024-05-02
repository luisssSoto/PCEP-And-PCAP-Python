"Arithmetic Exception"
'''Tree:
BaseException <- Exception <- ArithmeticError'''

try:
    print(6/0)
except ArithmeticError as e:
    print('Arithmetic Error: ', e)
    