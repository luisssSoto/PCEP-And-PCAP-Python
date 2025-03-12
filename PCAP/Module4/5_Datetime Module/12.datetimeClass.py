'''datetime class'''
import datetime

christmas = datetime.datetime(336, 12, 5, 8, 50, 59, 100_000, None)
print(christmas)
print(f'date: {christmas.date()} ')
print(f'time: {christmas.time()}')