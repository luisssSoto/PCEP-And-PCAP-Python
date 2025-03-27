'''strptime() from datetime class'''
from datetime import datetime
print(datetime.strptime("1994/02/04 14:01:03", "%Y/%m/%d %H:%M:%S"))

try:
    print(datetime.strptime("1994-02/04 14:01:03", "%Y/%m/%d %H:%M:%S"))
except ValueError as e:
    print("The data between both arguments must to match", e)
print()

'''strptime() from time module'''
import time
print(time.strptime("1994/02/04 14:01:03", "%Y/%m/%d %H:%M:%S"))
try:
    print(time.strptime("1994-02/04 14:01:03", "%Y/%m/%d %H:%M:%S"))
except ValueError as e:
    print("The data between both arguments must to match", e)
