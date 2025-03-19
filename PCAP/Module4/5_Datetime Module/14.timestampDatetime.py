"""timestamp() from datetime module"""
from datetime import datetime

dt = datetime(2000, 1, 1, 0, 0)
print(dt)
print(f"The seconds have passed since Jan 1 1970 until 2000 is {dt.timestamp()}")