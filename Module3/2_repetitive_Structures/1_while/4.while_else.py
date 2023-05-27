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

n=3
while n > 0:
    print(n)
    n-=1
    break #if you do this the code "else" will never execute
else:
    print("this is the end")   

print('We continue with the normal flow of the program')