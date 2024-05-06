""" Stack with a Procedural Approach """

# Define the stack
stack = []

# Define a function to push a value inside the stack
def push(value):
    stack.append(value)
    
# Define a function to pop the last value of the stack
def pop():
    lastValue = stack[-1]
    del stack[-1]
    return lastValue

for i in range(5):
    push(i)
    print(f'The value: {i} was added succesfully')
for i in range(3):
    print(f'The value {pop()} was pop so the stack is emptier: {stack}')