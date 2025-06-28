"""How to print an entire calendar"""
import calendar

print(calendar.calendar(2025))

# Parameters:
# 1. width -> space between columns
# 2. line -> space between each row
# 3. columns -> number of spaces between months
# 4. months -> number of columns (months)
print(calendar.calendar(2025, 1, 1, 4, 4))