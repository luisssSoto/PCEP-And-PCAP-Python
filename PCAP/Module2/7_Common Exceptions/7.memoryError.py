""" Memory Error """
'''Tree:
BaseException <- Exception <- MemoryError '''

import time

condition = 1
string = 'x'
while condition:
    try:
        string += string
        print(len(string))
        #time.sleep(1) # Note: comment this code to look the exception is launched faster
    except MemoryError as e:
        print('Memory Error: ', e)
        # Note: remember to get out the loop
        condition = False