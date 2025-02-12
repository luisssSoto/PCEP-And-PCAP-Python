'''Timestamp'''
from datetime import date
import time

#Create a date by one timestamp (a date in seconds since 1970 00:00:00
#until one any other date)

timestamp = time.time()
print(f'The seconds have passed since 1970 00:00:00 until now are: {timestamp}')

now = date.fromtimestamp(timestamp)
print(f'Today is: {now}')