"""map() function and lambdas"""
'''Map takes 2 arguments:
1. function() even a lambda
2. any iterable entity (tupla, generator, list etc..)
3. can takes more than 2 arguments'''

'''map() function applies to every element of the second 
argument (iterable object), the function which was passed 
in its firts argument, and returns an iterator/generator 
object'''

'''Put attention in how to access the iterator object'''

list1 = [x for x in range(5)]
list2 = list(map(lambda x : 2 ** x, list1))
print(list2)

for i in map(lambda x : x * x, list2):
    print(i, end=' ')