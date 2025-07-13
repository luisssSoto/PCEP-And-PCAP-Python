"""Final Test Module 4"""

# 1. lambda
y = lambda x: x ** x
print(y(3))
print()

# 2. lambda
addition = lambda x, y, z, w: x + y + z + w
print(addition(10, 20, 30, 40))
print()

# 3. lambda, map and tuple
l = [1,2,3]
t = tuple(map(lambda x: x ** x, l))
print(t)
print()

# 4. lambda, filter, list
t = (0,1,2,3,4,5,6)
l = list(filter(lambda x: x-0 and x-1, t))
print(l)
print()

# 5. yield
def I():
    s = "abcdef"
    for c in s[::2]:
        yield c

for x in I():
    print(x, end="")
print()

# 6. yield
def fun(n):
    s = "+"
    for i in range(n):
        s += s
        yield s

for i in fun(2):
    print(i, end="")
print()

# 7. 
def o(p):
    def q():
        return "*" * p
    return q

r = o(1)
s = o(2)
print(r() + s())
print()

# 8. reading a file
from os import strerror

try:
    stream = open(file="C:\\Users\\aleja\\PCEP-And-PCAP-Python\\PCAP\\Module4\\3_Working with Text and Binary Files\\text.txt", mode="rt", encoding="utf-8")
    character = stream.read(1)
    while character != "":
        print(character, end="")
        character = stream.read(1)
except IOError as e:
    print(f"e: {e}")
    print(f"erno: {strerror(e.errno)}, {e.errno}")
print()

# 9. errno.EXIST


# 10. bytearray
b  = bytearray(3)
print(b)

# 11. os
import os
 
os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('thumbnails')
os.chdir('thumbnails')
os.mkdir('tmp')
os.chdir('../')
 
print(os.getcwd())
print()

# 12. os
import os
 
os.mkdir('thumbnails')
os.chdir('thumbnails')
 
sizes = ['small', 'medium', 'large']
 
for size in sizes:
    os.mkdir(size)
 
print(os.listdir())
print()

# 13. date
from datetime import date
 
date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)
 
print(date_1 - date_2)

# 14. datetime
from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))
print()

# 15. calendar
import calendar
print(calendar.weekheader(2))
print()

# 16. Calendar
import calendar
 
c = calendar.Calendar()
 
for weekday in c.iterweekdays():
    print(weekday, end=" ")