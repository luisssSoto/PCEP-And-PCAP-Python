"""read() with arguments"""
'''read() with arguments allows us to say the maximum of the bytes that we want to
read, but read() must use only when we know if the memory we have will be enough 
compare with the bytes the file has'''

from os import strerror

try:
    byte_file = open(file='C:/pcep-and-pcap-python/pcap/module4/3_working with text files/fileBin.bin', mode='rb')
    data = bytearray(byte_file.read(5))
    for byte in data:
        print(byte, end=" ")
    print()
    print(f'length of data: {len(data)}') #you can find out if it read all the data by comparing the length
except IOError as ioe:
    print('Something was wrong', strerror(ioe.errno))

