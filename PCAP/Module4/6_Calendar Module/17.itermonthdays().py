"""itermonthdays()"""

from calendar import Calendar

c = Calendar()

for num in c.itermonthdays(2019, 11):
    print(f"number day: {num}", end=" ")

# Note: All the zeroes represent the days that don't belong
# the same month