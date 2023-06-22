'''Floor division'''
print("floor division", 2.5//2)

operand1,operand2=5,2
result=operand1 // operand2
print(operand1, '//', operand2, '=', operand1//operand2)
print()

"""Special Cases"""
'''We can add a unary value before the operand (- or +)'''
print("floor division always runs throw the floor of the origin result")
print(6//4)
print(6.//4)
print(-6//4)
print(6.//-4, "\n")

'''Floor division by zero "//" '''
print("It'll be an error:")
try:
    print(5//0)
except ZeroDivisionError:
    print("There was a division by zero \n")