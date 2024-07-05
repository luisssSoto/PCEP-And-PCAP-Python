"""Module Test"""
'''1.'''
class Vowels:
    def __init__(self):
        self.vowels = 'aeiouy'
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count == len(self.vowels):
            raise StopIteration
        self.count += 1
        return self.vowels[self.count - 1]

vowels = Vowels()
for i in vowels:
    print(i, end='')
print()

'''2.'''
any_list = [x for x in range(1, 5)]
print(any_list)
even_list = list(map(lambda n: n | 1, any_list))
print(even_list)

'''3.'''
def replace_spaces(replacement = '*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement

stars = replace_spaces('**')
print(stars('Something Completely Different '))

'''Note: Although the lambdas functions can be assign to any variable it is not a good practice, but
on the other hand typing def function() could have more lines of code, you need to decide the best
approach depends of the context'''