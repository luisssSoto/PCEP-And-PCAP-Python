"""Closures"""
'''The closures allows us to save the local variables inside another function which
is just inside of it, even if the external function doesn't exist anymore, the
inside function keeps the local variables inside of it'''

def outer(parameter):
    local = parameter

var1 = 1
outer(var1)
try:
    print(local)
    print(parameter)
except NameError as n:
    print(n.args) 

# So as you can see those variables aren't visibles since outside the function, but
# we can see those variables by using closure approach

def outer(parameter):
    local = parameter

    def inner(): #This is a closure
        return local
    return inner

var1 = 1
inside_function = outer(var1)
print(inside_function())
print()

'''We must to call a closure the same way it was declared: '''
def make_closure(parameter):
    local = parameter
    def power(parameter_pow):
        return parameter_pow ** local
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

'''Conclusion:
1. The closure can use an a freeze environment
2. The closure can modify its own behavior by taking external values
3. You can create any amount of different closures you want'''