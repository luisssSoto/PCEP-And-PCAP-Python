print("Compression List")
print("syntax: compressionList=[expression for elemento in list if conditional]")
#The code above it is the next below:
#for elemento in list:
  #  if conditional:
    #    expression

'''shorter way'''
compressionList=[i for i in range(5)]
print(compressionList)
compressionList=[i for i in compressionList if i % 2 != 0]
print(compressionList)

'''longer way'''
l=[]
for element in range(5):
    if element % 2 != 0:
        l.append(element)
print(l)
