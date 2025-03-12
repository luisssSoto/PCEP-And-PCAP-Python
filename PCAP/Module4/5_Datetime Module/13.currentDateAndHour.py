'''today() now() utc()'''
from datetime import datetime

# tzinfo establecido a None.
print(f'today: {datetime.today()}')

# si se desea se puede pasar un objeto de tipo tzinfo
print(f'now: {datetime.now()}')

# tzinfo establecido a None.
print(f'utc: {datetime.utcnow()}')