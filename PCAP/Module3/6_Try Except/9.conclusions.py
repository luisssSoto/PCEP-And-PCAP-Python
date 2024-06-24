"""Conclusions"""
'''1. block else will be executed if any exception is executed 
first'''

try:
    print('try')
except:
    print('exception')
else:
    print('else')
print()

'''2. block finally always will be executed'''
try:
    print('try')
    print(float('😑'))#Comment and uncomment this line to look the difference
except: 
    print('exception')
else:
    print('else')
finally:
    print('finally')

'''3. You can caught the object of any Exception and call the 
property args to look all the parameters pass into its
constructor of its class'''
class NewException(Exception):
    def __init__(self, message, number_exception = 1234):
        Exception.__init__(self, message, number_exception)

exception1 = NewException('Hi I am a new Exception')
print(exception1, exception1.args, sep=" | ")

try:
    raise NewException('Exception launched')
except NewException as e:
    print(e, e.args)
print()

'''4. always you can try some new things'''
try:
    assert __name__ == '__main__' #change the relational operator "!="
    print(__name__)
except AssertionError:
    print('Assertion Error')
else:
    print('else')
finally:
    print('finally')