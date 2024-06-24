"""final Test"""
'1.'
import math
try:
    print(math.sqrt(9))
except ValueError:
    print('Value Error')
else:
    print('else')
print()

'2.'
try:
    print(math.sqrt(-9))
except ValueError:
    print('Value Error')
else:
    print('else')
finally:
    print('finally')

'3.'
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError('friend Warning ⚠', 'red flag 🥅', 'hight probability')
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')