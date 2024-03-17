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
my_list = ['Mary', 'had', 'a', 'little', 'lamb']  
def my_list(my_list):
    try:
        del my_list[3]
    except TypeError:
        print('You can\'t delete a function object')
    my_list[3] = 'ram'
try:
    print(my_list(my_list))
except TypeError:
    print("It's not possible")



