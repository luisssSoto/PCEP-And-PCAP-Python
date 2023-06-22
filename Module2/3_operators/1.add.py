"""Operators in Python"""
print("Welcome to the operators")
print("The simplest expression is when you mix one data with another one:")

'''Add'''
print("add:", 2+2)

'''What about float numbers'''
operand1=5
operand2=10.3
result=operand1+operand2
print(operand1,'+',operand2,'=',result)

#As you can see the result is a float number because the rule "Integer vs Float Rule"
#The "Integer vs Float Rule" works in all operations except the division (/) because in this case
#the division always print float number and the integer division (//) only when we use integers the result will be
#an integer
print(10/5)
print(10//5)
print(10.0/5)