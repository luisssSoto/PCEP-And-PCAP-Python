"""Welcome For loop"""
print("Welcome For loop")
for i in range(10):
    print("The i's value is:", i)

#Sometimes you dont know what you should do inside a loop...
#you can type pass and this is all
for i in range(100):
    pass

print("\nrange with 2 arguments")
for i in range(2,10):
    print("i:", i)

print("\n range with 3 arguments")
for i in range(2,11,2):
    print("i:", i)

print("\nIn these cases  \"for\" won't work")
for i in range(1,1):
    print("It won't work")

for i in range(2,1):
    print("Here neither")

'''You can iterar to for cycle in reverse to:'''
for i in range(10, 2, -2):
    print('Im running in reverse!', i)

'''You can assign the value of a range function to one variable'''
var_range=range(5)
for i in var_range:
    print('var_range:', i-1)
else:
    print('var_range:',i)