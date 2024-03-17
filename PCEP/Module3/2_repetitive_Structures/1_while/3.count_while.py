print("While with a count variable")
count=5
while count != 0:
    print("number of times:", count)
    count-=1

'''This way doing the code easier to read but be careful about it'''
count=5
while count:
    print("number of times:", count)
    count-=1

print("\n Be careful with an infinite cycle:")
try:
    while True:
        print("Press ctrl+C to stop the program")
except KeyboardInterrupt:
    print("We got out from while")
print("Now we can continue \n")
