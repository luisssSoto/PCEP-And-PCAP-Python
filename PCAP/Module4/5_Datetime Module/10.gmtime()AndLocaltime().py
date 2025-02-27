'''gmtime() and localtime()'''
import time

'''gmtime() returns object struct_time in UTC and tm_isdst is always 0'''
print(time.gmtime())

'''localtime() returns an object structime with the local hour '''
print(time.localtime())