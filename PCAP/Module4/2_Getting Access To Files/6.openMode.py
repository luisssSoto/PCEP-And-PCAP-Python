"""Open Mode"""
'''In order to open a file, you must follow the next sintax:
This is the first sentence by working with streams'''
#stream = open(file, mode = 'r', encoding = None)

'''
1. open() function returns an object stream if it's successfully
2. file: the name of file you want to work with
3. mode: the open mode you want to use (you can ommit it, and its default value is 'rt')
4. encoding: for example UTF-8 (you can ommit it, and its default value depends of the platform used)'''

'''Open Mode
1. r reading mode
    the file associated with the stream must exist and needs to be readable
2. r+ reading and updating mode
    the file associated with the stream must exist and has permissions of writing
3. w writing mode
    the file associated with the stream doesn't need to exist, if so, a new file 
    will be created, but if the file exist the past content will be deleted
4. w+ writting and updating mode
    the file associated with the stream doesn't need to exist, if so, a new file
    will be created, but if the file exist the past content won't be deleted
5. a appending mode
    the file associated with the stream doesn't need to exist, if so, a new file
    will be created, but if the file exist the past content won't be deleted
    '''

'''Note:
if these rules above doesn't follow, an Exception will be generated '''