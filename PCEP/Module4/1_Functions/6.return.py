"""Functions - return"""
print("Welcome to return")

#1.function of return
def ends(n1):
    for i in range(n1):
        if i == 5:
            return
        print(i)

ends(6)
ends(10)
    
#2.function's return
def exponentiation(number,exp):
    result=number**exp
    return result

result=exponentiation(2,4)
print("exponentiation function:", result)