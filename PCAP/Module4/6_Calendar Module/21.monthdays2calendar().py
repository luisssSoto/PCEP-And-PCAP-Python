"""monthdays2calendar()"""
from calendar import Calendar

c = Calendar(6)
for week in c.monthdays2calendar(2025, 7):
    print(f"week: {week}")