'''weekday() method'''
'''0 -> Monday 6 -> Friday'''
from datetime import date

monday = date(2025, 2, 10)
print(monday)

print(monday.weekday())

'''isoweekday ISO 85601
1 -> Monday 7 -> Sunday'''
print(monday.isoweekday())