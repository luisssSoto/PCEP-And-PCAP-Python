"""Bitwise Operators"""
'''All these operators work with bits'''
'''&  (ampersand) - conjunction.
|  (barra vertical) - disyunction.
~  (tilde) - negation.
^  (signo de intercalación) - only in bit's level (xor).'''

bitAm=0b0010
theMask=2 #---> this number into binary is 0010
binMask=bin(theMask)
print('binMask',binMask,'\n')

'''Ampersand &'''
print("ampersand: &")
print("Checking my bit's state with \"&\"")
if bitAm & theMask:
    print("My bit is ready 'cause it's on")
    print(bitAm)
    print(bin(bitAm))
else:
    print("My bit is not ready 'cause it's off")

#Explanation &:
#bitAm=           10
#theMask=         10
#bitAm&=theMask   10

'''Negation ~'''
print("\nnegation: \"~\"")
bitNeg=0b0010
print("Reset my bit's state with \"& and ~\"")
bitNeg &= ~theMask
print(bitNeg)
print(bin(bitNeg))

#Explanation & and ~:
#bitNeg=              10
#~theMask=            01
#bitNeg&=~theMask     00


print('\ndisjunction "|"')
bitDis=0b0010
print('Assign your bit to 1')
bitDis|=theMask
print(bin(bitDis))

#Explanation |:
#bitDis=           10
#theMask=          10
#bitDis|=theMask   10

print('\nexclusion "^"')
bitExc=0b0010
print('Negation of your bit')
bitExc^=theMask
print(bitExc)
print(bin(bitExc))  

#Explanation ^:
#bitExc=          10
#theMask=         10
#bitExc^=theMask  00