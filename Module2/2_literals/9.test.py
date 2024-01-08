'''Instructions:
Type as a comment the number that you expect the print
function will show on screen'''

d=7
b=bin(d)#111
o=oct(d)#7
h=hex(d)#7

print(d, b, o, h, sep='|')

fourty_five=0b101101
print(bin(fourty_five))

print(fourty_five//8)
print(fourty_five*8)
print(fourty_five>>3)#0b101101 ->000101
print(fourty_five<<3)#0b101101 ->101101000


'''Which of these is not available'''
print(20*10**6)
print(20E6) #-> Remember always is a float
print(50*10**6.5)
# print(20E6.5)