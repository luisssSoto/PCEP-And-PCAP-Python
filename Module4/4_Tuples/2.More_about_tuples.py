"""Tuples what they can do"""
print("Welcome to tuples instructions")
tuple1=('tuple', 1,None, True, 14.6)

#iteration
for i in range(len(tuple1)):
    print("Element:", i, tuple1[i])

#len() function
print("tuple's length is:", len(tuple1))

#in and not in
print('Is the element "None" in the tuple?', None in tuple1)
print('Is the element "None" not in the tuple?', "None" not in tuple1)

#+
tuple2=tuple1+('list', 'of', 'Strings')
print('tuple2:',tuple2)

#*
tuple3=tuple2*3
print(tuple3)

#Assign values each other
t1=('a','e','i','o','u')
t2=2,4,6,8
t3=('tuple3',[1,2,3], (3.14,4.5))

t1,t2,t3=t2,t3,t1
print(t1,"\n", t2,"\n", t3)

#If you combine a tuple with another one but in some one of them there is
#a tuple, set, dictionary or list, so the format will be the next
t4=('two','words')+t2
print('t4:',t4)