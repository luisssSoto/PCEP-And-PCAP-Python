"""Tuples what they can do"""
print("Welcome to tuples instructions")
tuple1=('tuple', 1, None, True, 14.6)

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

#If you combine a tuple with another one but in someone of them there is
#a tuple, set, dictionary or list, so the format will be the next
t4=('two','words')+t2
print('t4:',t4)

"""Remember the changes in situ can't be possible in tuples """
try:
    del t4[0]
except TypeError:
    print('The code below is possible because there is not a change in situ')
    del t4
    try:
        print(t4)
    except NameError:
        print('This element has gone')
      
'''It's the same result when we multiplicate them'''  
tupletest=((1,2),(3,4),(5,6))
t = tupletest*3
print('t', t)

'''Note: you can convert any iterable data to a tuple or vice versa'''
list1=[1,2.5,3]
tuple1=tuple(list1)
print(tuple1)
print(type(tuple1))