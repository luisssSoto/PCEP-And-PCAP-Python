"""Greater Number"""
n1=int(input("Introduce any number you want, or 0 if you want to stop this program:"))
nGreater=-9999999
while  n1 !=0:
    if n1 > nGreater:
        nGreater = n1
    n1=int(input("Introduce any number you want, or 0 if you want to stop this program:"))
print("The greater number is:", nGreater,"\n")

#It's not necesary to type anything at the end of the condition, like if statement
#But you need to be clear 
print("This way is shorter to code")
n1=int(input("Introduce any number you want, or 0 if you want to stop this program:"))
while  n1:
    if n1 > nGreater:
        nGreater = n1
    n1=int(input("Introduce any number you want, or 0 if you want to stop this program:"))
print("The greater number is:", nGreater, "\n")

#Remember the last code works 'cause False=0 and True= any value different 0