'''While and else'''
print("while and else")

n=3
while n > 0:
    print(n)
    n-=1
else:
    print("this is the end")

#Even though the block while never work, the block else always will be execute except if you add a break
n=0
while n > 0:
    print(n)
    n+=1
else:
    print("this is the end")

'''We can try it but this time with "break" '''
n=3
while n > 0:
    print(n)
    n-=1
    break #if you do this the code "else" will never execute
else:
    print("this is the end")   

print('We continue with the normal flow of the program')


'''But you need to entry in the loop while to works the break, 
if not never will be execute the while and break'''

even=8
while even % 2 != 0:
    print(even)
    break
else: print('This code is the only one will work')
    

         