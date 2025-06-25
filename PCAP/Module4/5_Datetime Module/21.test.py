"""Final Test Section"""

# 1. 
from datetime import time
t = time(14, 53)
print(t.strftime("%H: %M: %S:"))

# 2. 
from datetime import datetime
 
dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)
 
print(dt1 - dt2)
