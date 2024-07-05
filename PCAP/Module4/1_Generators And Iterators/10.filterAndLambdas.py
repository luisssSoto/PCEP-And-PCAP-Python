"""filter() function and lambdas"""
'''this functions returns an iterator object like map() function but in this case,
exist a filter so all the validations that be true will pass the filter succesfully 
and in this case they will be added to the list "filtered_data"'''

from random import seed, randint

seed()
data = [randint(-10, 10) for x in range(5)]
filtered_data = list(filter(lambda x : x > 0 and x % 2 == 0, data))

print(data)
print(filtered_data)