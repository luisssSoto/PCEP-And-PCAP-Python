#Even though the block for never works, the block else always will be execute except if you add a break
print("\nFor-else")
i=111
for i in range(2,1):
    print(i)
else:
    print("else", i)

#-------------#
for i in range(1,3):
    print(i)
else:
    print("else", i)

#-------------#
for i in range(1,3):
    print(i)
    break #-----> if you do this the code won't execute the block else
else:
    print("else", i)
print('We continue with the normal flow of the program')
