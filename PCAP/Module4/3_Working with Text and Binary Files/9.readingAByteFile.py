"""Reading a Byte file"""
'''readinto() method
1. doesn't return any object instead fill one was created with the data of the file.bin
2. tries to fill all the amount of bytes that were passed in its argument
but if there are more bytes in the file.bin than the argument the program will
stop and the response will show that the file was partially readed
3. the method returns the number of bytes readden successfully'''

from os import strerror

data = bytearray(10)
print(f'data: {data}')
print(type(data))
print(len(data))
print()
try:
    byte_file = open(file='C:/pcep-and-pcap-python/pcap/module4/3_working with text files/fileBin.bin', mode='rb')
    amount_data = byte_file.readinto(data)
    print(f'amount of data: {amount_data}')
    for byte in data:
        print(byte, end=" ")
    byte_file.close()
except IOError as ioe:
    print('Something was wrong', strerror(ioe.errno))