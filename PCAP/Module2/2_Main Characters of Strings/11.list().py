''' list() function '''
string3 = '1234'
listString3 = list(string3)
print(listString3)

#Note: list() function works whit more literals not only with strings
tuple1 = (1, 'a', True)
print(list(tuple1)) 

s = set()
for i in range(5):
    s.add(i)
print(list(s))

