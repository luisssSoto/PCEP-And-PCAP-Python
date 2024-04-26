"""Casting to strings and vice versa"""
'''Casting is always possible if the value to cast is allow'''

trees = 500
amountAfterTax = 15.5

print(str(trees) + ' ' + str(amountAfterTax))

strNotNumber = '5.378'
print(float(strNotNumber))

'''Remember the value needs to be allow'''
onomatopoeia = 'pum!'
try:
    print(int(onomatopoeia))
except ValueError:
    print('that value can\'t cast to int')

s1 = '¿Dónde están las nieves de antaño?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[1])
