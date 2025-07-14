"""Test"""

# Secure
import math
print(math.pi)

# A little bit insecure
from math import pi
print(pi)

# Totally insecure
from math import *
print(e)
e = 'vowel'
print(e)

# aliasing
import math as m
print(m.pi)

from math import pi as p, sin as seno, cos as coseno
print(seno(p))
print(coseno(p))
