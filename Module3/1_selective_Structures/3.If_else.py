"""Make decisions if-else"""
planA = "Let's go outside"
planB = "Let's watch a serie on \"Netflix\""
isSafety = False

if isSafety == True:
    print(planA)
else:
    print(planB)

print("We continue with the normal flow of the program")

'''This way is easier and is the same'''
if isSafety:
    print(planA)
else:
    print(planB)
print("We continue with the normal flow of the program")

#Note: The last part was possible 'cause the default value
#of the "if" is True