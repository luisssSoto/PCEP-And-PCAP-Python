"""Conclusions"""

# 1. module datetime and date class
from datetime import date
d = date(2020, 12, 2)
print(d)
print()

# 2. attributes of date object, they are only for reading
print(d.day)
print(d.month)
print(d.year)
print()

# 3. today() method
print(date.today())
print()

# 4. Creating an object date with a timestamp as an argument
import time
timestamp = time.time()
print(f"Amount of seconds have passed since January 1 1970 until now: {timestamp}")
new_obj = date.fromtimestamp(timestamp)
print(new_obj)
print()

# 5. Constructor time wich belongs to datetime module
from datetime import time as t
obj_time = t(15, 34, 3, 2)
print(obj_time)
print(obj_time.hour)
print(obj_time.min)
print(obj_time.second)
print(obj_time.microsecond)
print()

# 6. method sleep() from time
time.sleep(3)
print("Hello folks")
print()

# 7. datetime class from datetime
from datetime import datetime
unix_dt = datetime(1990, 1, 1, 23, 0, 0, 0)
print(unix_dt)
print()

# 8. directives with strftime
d = date(1994, 2, 4)
print(d.strftime("%Y-%m-%d"))
print()

# 9. Perform calculations
d2 = date(1992, 11, 3)
d3 = d - d2
print(f"The difference in days from {d2} to {d} is: {d3}")
print(f"another interesting calculations: {d3 * 2}")