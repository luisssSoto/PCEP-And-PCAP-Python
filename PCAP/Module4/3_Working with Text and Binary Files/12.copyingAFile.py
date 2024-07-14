"""Copying Files"""

from os import strerror

src_name = input('Type the name of the file: ')

try:
    src = open(file="C:/pcep-and-pcap-python/pcap/module4/3_working with text files/" + src_name, mode='rb')
except IOError as e:
    print("It can't open the file", strerror(e.errno))
    exit(e.errno)

dst_name = input('Type the location of the file: ')

try:
    dst = open(file='C:\\pcep-and-pcap-python\\pcap\\module4\\3_working with text files\\' + dst_name, mode='wb')
except IOError as e:
    print("It can't create the file in the destination", strerror(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0

try:
    readin = src.readinto(buffer)
    print(f'readin: {readin}')
    while readin > 0:
        written = dst.write(buffer[:readin])
        print(f'written: {written}')
        total += written
        readin = src.readinto(buffer)
        print(f'readin: {readin}')
except IOError as e:
    print("It can't create the file in the destination", strerror(e.errno))
    exit(e.errno)

print('Total of bytes written successfully:', total)
src.close()
dst.close()