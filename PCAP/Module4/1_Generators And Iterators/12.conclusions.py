"""Conclusions"""
'''1. iterator has two important methods plus the constructor'''
class MyIterator:
    def __init__(self, parameter):
        self.local = parameter
        self.count = 0
        self.value = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.value += 1
        if self.count == self.local:
            raise StopIteration
        else:
            self.count += 1
            return self.value
        

my_iterator1 = MyIterator(10)
print(my_iterator1)
for i in my_iterator1:
    print(i, end=" ")
print()

'''2. yield'''
def yield_function(potencia):
    for i in range(potencia):
        yield i ** potencia
        
list_yield = list(yield_function(5))
print(list_yield)

'''3. conditional expression'''
dessert = 'cake'
recipe = ['fluor' if dessert == 'cake' else 'ask for more details']
print(recipe)

'''4. generator by building a compression list'''
for k in ('🍆🍇' for j in range(8)):
    print(k)
print()

'''5. lambda'''
def example(function, parameter):
    print(function(parameter))

example(lambda word: word.capitalize(), 'alex soto')
print()

'''6. map() function do a copy of the list by applying all the
elements of the list, than function'''
numbers_and_letters = ['odd' if l % 2 != 0 else str(l) for l in range(5)]
print(numbers_and_letters)
new_list = list(map(lambda value: value.isdigit(), numbers_and_letters))
print(new_list)
print()

'''7. filter() function do a copy of all the elements that be True '''
wild_animals = ['cocodrile', 'anaconda', 'shark']
animals = ['cat', 'dog', 'fish'] + wild_animals
for domestic_animal in filter(lambda animal: len(animal)<=4, animals):
    print(domestic_animal)
print()

'''8. closures'''
def close_tag(tag):
    begin_tag = tag
    end_tag = tag[0] + '/' + tag[1:]
    def adding_word(word):
        return begin_tag + word + end_tag
    return adding_word

title = close_tag('<h1>')
complete_tag = title('Module 4 Python')
print(complete_tag)