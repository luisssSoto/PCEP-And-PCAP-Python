"""read()"""

'''Without arguments it tries to read all the content of the 
file by modifying an recent created object from the bytes class
But it is immutable not like bytearray()'''

from os import strerror

try:
    byte_file = open(file='C:/pcep-and-pcap-python/pcap/module4/3_working with text files/fileBin.bin', mode='rb')
    reading = byte_file.read()
    print('reading:', reading)
    print()
    data = bytearray(reading)
    for byte in data:
        print(hex(byte), end=' ')
except IOError as ioe:
    print('something was wrong', strerror(ioe.errno))