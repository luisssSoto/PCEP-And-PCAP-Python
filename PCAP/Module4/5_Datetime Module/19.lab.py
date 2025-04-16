"""Lab"""
# 1. datetime object Nov-04_2020 14:53:00
import datetime

dt = datetime.datetime(2020, 11, 4, 14, 53, 0, 0)
print(f"datetime object: {dt}")

# 2. call strftime to format the recent object datetime like the next format:
# 2020/11/04 14:53:00

st = dt.strftime("%Y/%m/%d %H:%M:%S")
print(st)

# 3. 20/November/04 14:53:00 PM
st1 = dt.strftime("%y/%B/%d %H:%M:%S %p")
print(st1)

# 4. Wed, 2020 Nov 04
st2 = dt.strftime("%a, %Y %b %d")
print(st2)

# 5. Wednesday, 2020 November 04
st3 = dt.strftime("%A, %Y %B %d")
print(st3)

# 6. Día de la semana: 3
print(dt.strftime("Dia de la semana: %w"))

# 7. Día del año: 309
print(dt.strftime("Dia del año: %j"))

# 8. Número de semana en el año: 44
print(dt.strftime("Numero de semana en el año: %W"))