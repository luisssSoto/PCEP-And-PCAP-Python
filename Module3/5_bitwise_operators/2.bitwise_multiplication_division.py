"""Bitwise Operations"""
print("\nBitwise Operations")
v17=0b10001
print(v17)
div17=v17 >> 1 #----->v17 is equal to whole division "//" 2 to decimal system 17//2=8
print(div17)

#Explanation:
#v17=   10001
#1=     00001
#div17= 01000 = 8

'''You can type in a shorter way:'''
v17>>=1
print(v17,end='\n')


mul17=v17 << 2#--->is like multiply for 4 decimal system 17*4=68
print(mul17)

#Explanation:
#v17=   10001
#2=     00010
#mul17= 1000100 = 68

'''Shorter way'''
v17<<=2
print(v17)
print()


'''Remember don't matter with what kind of number you work all depend for what operator
you use to do the expression'''

"""The expression will be take as a binary numbers"""
valueBin1=81#0b1010001
valueBin2=2#0b10
resultBin=valueBin1>>valueBin2
print(resultBin)
print(bin(resultBin))

valueBin1=81#0b1010001
valueBin2=6#0b110
resultBin=valueBin1<<valueBin2
print(resultBin)
print(bin(resultBin))

"""The expression will be take as a decimal numbers 'cause the operands 
although the values were writen as binary number"""
valueBin1=0b1010001
valueBin2=0b10
resultBin=valueBin1//valueBin2
print(valueBin1, '//', valueBin2, '=', resultBin)

valueBin1=0b1010001
valueBin2=0b110
resultBin=valueBin1*valueBin2
print(valueBin1, '*', valueBin2, '=', resultBin)