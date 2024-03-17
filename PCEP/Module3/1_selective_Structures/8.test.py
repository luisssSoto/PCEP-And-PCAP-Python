'''You can put the whole sentence "if" in on line if there is only one instruction'''
if type('string') == type('another String'): print('Don\'t forget you can put all the body if in one line')
else: print('Another comment')

'''The most of Python's function needs to keep the value of a variable if not the return of
the function will loose'''
greater, shorter = 58.9, 2.13
maxValue=max(greater,shorter)
minValue=min(shorter,greater)
print(f'{maxValue} is greater than {minValue}')

print('''Remember there is a Selective Structure''')
print('only if')
floatNumber=3.3
if type(floatNumber)==(float): print("It's possible")

print('\n', 'if else')
if floatNumber >= 5: print(f'{floatNumber} is >= to 5')
else: print(f'{floatNumber} is < than 5')

print("\n", 'if, elif, and else')
if floatNumber > 5: print('🤔')
elif floatNumber == 3.3: print("🥳")
else: print('😒')