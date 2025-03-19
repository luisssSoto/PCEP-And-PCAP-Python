"""strftime()"""
import time

seconds = 1946706400
st = time.gmtime(seconds)
print(st)

# global time
print(time.strftime("%Y/%m/%d %H:%M:%S", st))
# local time
print(time.strftime("%Y/%m/%d %H:%M:%S"))