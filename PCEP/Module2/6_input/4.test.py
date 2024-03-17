'''Remember that you can apply the sum (+) and multiplication
 (*) symbol to strings but first one is not commutative
 and last one it is'''
 
var1='1'
listen=int(input('Type a number: '))

'''Commutative'''
print(var1*listen)
print(listen*var1, end='\n')

'''No Commutative'''
listen=(str(listen))
print(var1+listen)
print(listen+var1)