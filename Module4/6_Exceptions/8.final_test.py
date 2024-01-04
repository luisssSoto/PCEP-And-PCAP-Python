dictionary = {}
my_list = ['a', 'b', 'c', 'd'] 
for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], ) 
for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0])

print(dictionary)
dictionary.update({'e': ('e',)})
print(dictionary)
dictionary['f']=('f',)
print(dictionary)

'''2. What will be the result when Python executes this code'''
# def func(a, b):
#     return a ** a 
# print(func(2))

'''3. What will be the result of the code below'''
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return  
# print(fun(fun(2)) + 1)

'''4. What will happen when execute the next code'''
my_lis = ['Mary', 'had', 'a', 'little', 'lamb']  
def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'
print(my_list(my_lis))



