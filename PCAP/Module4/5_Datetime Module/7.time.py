'''Class time'''
from datetime import time

obj_time = time(21, 36, 58, 1000)
print(obj_time)
print(f'hour: {obj_time.hour}')
print(f'minute: {obj_time.minute}')
print(f'second: {obj_time.second}')
print(f'microsecond: {obj_time.microsecond}')