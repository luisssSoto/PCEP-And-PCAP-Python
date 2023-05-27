"""Greater and less number with Python's functions"""
print("The max() and min() functions in Python")
n1=int(input("Introduce a number: "))
n2=int(input("Introduce a number: "))
n3=int(input("Introduce a number: "))

numGreater=max(n1,n2,n3)
print("The greater number is: ", numGreater)
numLess=min(n1,n2,n3)
print("The less number is:", numLess, "\n")

print("round() function")
numFloat=50.8965
print(numFloat, "now let's round it:", round(numFloat))

print('another example')
listNumbers=[10.4,3.9,32.333,5.2,67.233,1.7]
greaterNumber=max(listNumbers)
print(greaterNumber)
roundIt=round(greaterNumber)
print(roundIt,end='\n')

lessNumber=min(listNumbers)
print(lessNumber)
roundIt=round(lessNumber)
print(roundIt)



