""" Key Error """
''' Tree:
BaseException <- Exception <- LookupError <- KeyError'''

genius = {'Steve Jobs': 'Apple', 'Bill Gates':'Microsoft' }

try:
    print(genius['Linus Torvalds'])
except KeyError as e:
    print('Key Error: ', e)