"asctime() and mktime()"
import time

timestamp = 15656516451
st = time.gmtime(timestamp)
print(st)

'''asctime receives as argument an object of struct_time'''
print(time.asctime(st))

seconds_have_passed = time.time()
lc_time = time.localtime(seconds_have_passed)

if time.asctime() == time.asctime(lc_time):
    print('The asctime() function without argument gives us current date')
    print(time.asctime())

'''mktime receives as argument an object of struct_time'''
print(time.mktime(st))