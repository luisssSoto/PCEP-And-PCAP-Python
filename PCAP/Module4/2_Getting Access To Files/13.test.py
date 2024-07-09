"""Test"""

'''1. create a file and write'''
stream = open(file='C:\\Users\\AlexSoto\\Desktop\\newFile.txt', mode='wt')
stream.close()

'''2. errno.EACCS'''
import errno, os
number_error = errno.EACCES
description_error = os.strerror(number_error)
print(f'number of error: {number_error} \ndescription error: {description_error}')

'''3. wich will be the result:'''
try:
    stream = open(file='anyfile.txt', mode='rb')
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print('the file does not exist')
    else:
        print('the file exist')
