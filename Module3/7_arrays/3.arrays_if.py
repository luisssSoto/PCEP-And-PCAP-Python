print("Looking the odd numbers")
array1=[[row for row in range(10)] for row in range(5)]
print(array1)
print()

for col in array1:
    for row in col:
        if row % 2 != 0:
            print(row, end=' ')
print(array1)
print()

'''shorter way'''
evenNumberArray=[[i for i in range(11) if i % 2 == 0 ]for j in range(5) if j % 2 != 0]
print(evenNumberArray)