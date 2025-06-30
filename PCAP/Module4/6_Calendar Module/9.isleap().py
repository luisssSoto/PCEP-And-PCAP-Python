"""isleap()"""

from calendar import isleap

year = 2020
if isleap(year) == True:
    print(f"year: {year} is a leap year")
else: 
    print(f"year: {year} is NOT a leap year")