"""Functions you need to call them"""

def substraction(minuend, sustraend):
    result = minuend - sustraend
    return result

print(substraction(5,2))

#Rules:
#1.Declare function first and then, call it
#2.Don't put the same name at the function and the variable --->this is allow but...look at the nex code:

def msg():
    return "The message is...."

print(msg())
msg="Hi"
print(msg)

print(msg())#This will be a tyme error execution

#Now are you understanding?
