'''Creating timedelta objects'''
from datetime import timedelta
delta = timedelta(weeks=2, days=3, hours=4)
print(delta)

# This object only save days, seconds and microseconds internally; 
# so that, all the data became in the valid attributes, for example
# the weeks in days, the hours and minutes in seconds, and miliseconds
# in microseconds
print(f"days: {delta.days}, seconds: {delta.seconds} and microseconds {delta.seconds}")
print()

'''Available operation in datetime'''
from datetime import date, datetime

'''multiplication *'''
delta2 = delta * 2
print(delta2)

'''addition'''
d = date(1991, 2, 5) + delta2
print(d)

dt = datetime(1991, 2, 5, 10, 5) + delta2
print(dt)

'''You should read the official documentation to know about more
operations available'''