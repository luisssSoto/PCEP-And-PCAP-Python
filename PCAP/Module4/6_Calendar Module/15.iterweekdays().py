"""iterweekdays()"""

import calendar

c = calendar.Calendar()

"""iterweekdays"""
for day in c.iterweekdays():
    print(f"day: {day}", end=" ")