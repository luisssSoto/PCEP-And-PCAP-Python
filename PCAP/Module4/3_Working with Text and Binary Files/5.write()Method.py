"""write() method"""
'''it waits only one argument (one string), you must remember use the correct open
mode to open the file (w) otherwise the connection will fail, and it's important 
knowing that write() method doesn't add the new line so you need to add it (\n)'''

'''1. character by character'''
from os import strerror

try:
    file = open(file='C:/pcep-and-pcap-python/pcap/module4/3_working with text files/newText.txt', mode='wt', encoding='utf-8')
    for i in range(10):
        string = 'line # ' + str(i + 1) + '\n'
        for character in string:
            file.write(character)
        print(string, end='')
    file.close()
except IOError as ioe:
    print('Something was wrong', strerror(ioe.errno))

'''2. line by line'''
try:
    file = open(file='C:/pcep-and-pcap-python/pcap/module4/3_working with text files/newText.txt', mode='wt', encoding='utf-8')
    for i in range(10):
        file.write('line #' + str(i + 1) + '\n')
    file.close()
except IOError as ioe:
    print('Something was wrong', strerror(ioe.errno))

