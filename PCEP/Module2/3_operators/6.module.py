'''Module'''
print("module:", 10%3)

operand1,operand2=15,7
print(operand1, '%', operand2, '=', operand1%operand2)

'''Division by zero is imposible too for module %'''
print("It'll be an error:")
try:
    print(5%0)
except ZeroDivisionError:
    print("There was a division by zero \n")
    
'''What about when the first number is shorter than the second one'''
shorter=5
larger=15
result=shorter%larger
print(shorter,'%',larger,'=',result)