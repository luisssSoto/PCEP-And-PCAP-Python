"""Greater and less number with Python's functions"""
print("The max() and min() functions in Python")
n1=int(input("Introduce the first number: "))
n2=int(input("Introduce the second number: "))
n3=int(input("Introduce the first number: "))

numGreater=max(n1,n2,n3)
print("The greater number is: ", numGreater)
numShorter=min(n1,n2,n3)
print("The shorter number is:", numShorter, "\n")

print("round() function")
numFloat=50.8965
print(numFloat, "now let's round it:", round(numFloat))

print('another example')
listNumbers=[10.4,3.9,32.333,5.2,67.49,1.6]
greaterNumber=max(listNumbers)
print(greaterNumber)
roundIt=round(greaterNumber)
print(roundIt,end='\n')

shorterNumber=min(listNumbers)
print(shorterNumber)
roundIt=round(shorterNumber)
print(roundIt)