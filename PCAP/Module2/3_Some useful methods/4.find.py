'''.find() method'''
print('panda'.find('a'))
print('panda'.find('da'))

# it's safer to use index() 'cause if the element is not in the string
# won't be any exception, but if you want to find only one match the
# in instructions is faster

print('panda'.find('o'))

'''.find() two parameters'''
print('panda'.find('a', 2))

'''.find() thre parameters'''
print('panda'.find('a', 2, 4))

'''using .find() to find all the matches'''
string = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Duis semper mauris quis ullamcorper molestie. 
Aliquam est dui, convallis vel tincidunt et, mollis eget massa. 
Donec metus tortor, iaculis id pharetra ac, interdum molestie nibh. 
Phasellus luctus lorem vel tellus volutpat tincidunt at sed massa. 
Suspendisse sodales lorem est, quis rutrum mi varius vitae. 
Donec nunc felis, sollicitudin vitae rhoncus at, tristique id sapien. 
Nunc risus sem, fermentum at gravida at, fringilla et tellus. 
Maecenas dignissim varius blandit. Phasellus mi odio, porttitor id varius sit amet, fermentum venenatis risus.'''

listOfMatches = []
start = 0
index = 0
while index != -1:
    index = string.find('lorem', start)
    start += index + 1
    if index != -1:
        listOfMatches.append(index)

print(listOfMatches)

# Note: all these methods are not compatible with lists or other litera