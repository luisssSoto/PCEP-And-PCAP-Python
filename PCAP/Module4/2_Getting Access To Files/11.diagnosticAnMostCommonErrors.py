"""Diagnostic and most common errors"""
'''Exist a module that helps us to identify which error is, but you must to import it:
errno(error number) and then call any of its constants which gives us a number of error,
but on the other hand errno property gives us the number of error which we have'''

import errno

try:
    stream = open('C:\\Users\\AlexSoto\\Desktop\\fileTst.txt', 'rt')
    # Proccesing the stream
    print('The file is opened')
    stream.close()
    print('The file is closed')
except Exception as exc:
    if exc.errno == errno.EMFILE:
        print("The file doesn't exist")
    elif exc.errno == errno.EACCES:
        print('Permission denied')
    elif exc.errno == errno.EBADF:
        print('Number of file incorrect, try to open the file first')
    elif exc.errno == errno.EEXIST:
        print('File exist')
    elif exc.errno == errno.EFBIG:
        print("File too big")
    elif exc.errno == errno.EISDIR:
        print("It's a directory")
    elif exc.errno == errno.EMFILE:
        print('Too many files opened')
    elif exc.errno == errno.ENOENT:
        print("The file or directory doesn't exist")
    elif exc.errno == errno.ENOSPC:
        print("There is not space in the device")
    else:
        print(f'The number of error is: {exc.errno}')

'''But in order to avoid writing all of these code above you can try this approach:
the function receives a number of error but at first you need to import it '''
from os import strerror

try:
    stream = open('C:\\Users\\AlexSoto\\Desktop\\fileTst.txt', 'rt')
    # Proccesing the stream
    print('The file is opened')
    stream.close()
    print('The file is closed')
except Exception as exc:
    print('Something happened:', strerror(exc.errno))
    print('Number of error:', exc.errno)