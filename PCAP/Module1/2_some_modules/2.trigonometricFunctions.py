"""Trigonometric Functions"""

from math import radians, degrees, sin, cos, tan

deg = 90
rad = radians(deg)

print(sin(rad))
print(cos(rad))
print(tan(rad))
print()

from math import asin, acos, atan
print(asin(sin(rad)))
print(acos(cos(rad)))
print(atan(tan(rad)))
print()

from math import sinh, cosh, tanh
print(sinh(rad))
print(cosh(rad))
print(tanh(rad))
