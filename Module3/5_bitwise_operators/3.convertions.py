'''Now if you want to know what is the correct expression to get the same results in
between the binary and decimal expressions you only need to convert one of the value
between its contrapart'''

print('Bits operations to Decimal operations')
print('Bits operation >>')
bin1=0b0101111101
bin2=0b100
newResultBin=bin1>>bin2
print(newResultBin)
print(bin(newResultBin))

print('Decimal operation //')
dec1=0b0101111101
dec2=16#--->0b100=4---->2**4=16
newResultBin=dec1//dec2
print(newResultBin)
print(bin(newResultBin), '\n')

print('Bits operation <<')
bin1=0b10
bin2=0b1100
newResultBin=bin1<<bin2
print(newResultBin)
print(bin(newResultBin))

print('Decimal operation *')
dec1=0b10
dec2=4096#--->0b1100=12---->2**12=4096
newResultBin=dec1*dec2
print(newResultBin)
print(bin(newResultBin), '\n')

print('Decimal operations to Bits operation')
print('Decimal operation *')
dec1=48
dec2=4
newResultDecimal=dec1*dec2
print(newResultDecimal)
print(bin(newResultDecimal))

print('Bits operation <<')
dec1=48
dec2=2
newResultDecimal=dec1<<dec2
print(newResultDecimal)
print(bin(newResultDecimal),'\n')

print('Decimal operation //')
dec1=456
dec2=32
newResultDecimal=dec1//dec2
print(newResultDecimal)
print(bin(newResultDecimal))

print('Bits operation >>')
dec1=456
dec2=5
newResultDecimal=dec1>>dec2
print(newResultDecimal)
print(bin(newResultDecimal))