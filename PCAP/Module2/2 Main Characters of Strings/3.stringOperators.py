"""string Operators"""

'''+'''
valueA = 'a'
valueB = 'b'

print(valueA + valueB)
print(valueB + valueA)
# As you can see the "+" operator is not commutative
# like its contrapart mathematic

'''*'''
print(valueA * 3)
print(3 * valueA)

'''+= and *= ''' 
fullName = ''
firstName = 'Alejandro'
lastName = 'Soto'
fullName += firstName + ' ' + lastName
print(fullName)