"""Make a decisions elif"""

hungry=None

if hungry:
    print("I'll eat a couple of tacos")
elif hungry == False:
    print("I'll eat a few chips")
else:
    print("I'm going to visit my parent's house and...")

print("I'll be programming in Python")

'''But what about we cast the var "hungry" to bool type'''
hungry=bool(None)
if hungry:
    print("I'll eat a couple of tacos")
elif hungry == False:
    print("I'll eat a few chips")
else:
    print("I'm going to visit my parent's house and...")
print('The flow of the program runs normal')