'''ctime()'''
import time
from datetime import date

seconds = time.time()
print(seconds)

# ctime() receives seconds and return the date
today = time.ctime(seconds)
print(today)

# ctime() without arguments
print(time.ctime())

# ctime() it's gives us more detail about the date
print(date.fromtimestamp(seconds))