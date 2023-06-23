"""Logic Operators"""

print("Welcome to the \"not\" Negation unary!")
print(not True)
print()

print('Welcome to the "and" Conjunction binary')
if 1 == 1 and 1 > 0:
    print(True, "because all of the conditions were true")
else:
    print(False, "because at least one condition was false")
print()

print('Welcome to the "or" Disjunction binary')
if 1 == 1 or 1 < 1:
    print(True, "because at least one condition was true")
else:
    print(False, "because nothing condition was true")

#Remember the True always is any value diferent to 0 and None but if you cast it
#the True value will be 1:
var = True
print(int(var))
var+=1
print(var)

var='any value'
castToBool=bool(var)
print(castToBool)