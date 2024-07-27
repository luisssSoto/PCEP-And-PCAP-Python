"""Conclusions"""
'''1. read(number bytes/characters)'''

from os import strerror

try:
    # text mode
    #stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/london bridge.txt", mode="rt", encoding="utf-8")
    # binary mode
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/london bridge.txt", mode="rb")
    entire_file = stream.read()
    print(f"The entire file: {entire_file}")
    stream.close()
except IOError as i:
    print("Something happend:", strerror(i.errno))

'''2. readline() only text files'''
try:
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/london bridge.txt", mode="rt", encoding="utf-8")
    one_line = stream.readline()
    print(f'one line: {one_line}')
    stream.close()
except IOError as i:
    print("We couldn't open the file 'cause of:", strerror(i.errno))

'''3. readlines(number of lines) or readlines()'''
try:
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/london bridge.txt", mode="rt", encoding="utf-8")
    five_lines = stream.readlines(500) # 500 bytes
    print(f"five lines: {five_lines}")
    print(f'number of lines: {len(five_lines)}')
    rest_of_lines = stream.readlines() # the rest of all lines
    print(f"all the lines:", rest_of_lines)
    stream.close()
except IOError as i:
    print("Something ocurred bad", strerror(i.errno))

'''4. readinto(bytearray) only bytes'''
number_of_bytes = bytearray(1000)
try:
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/london bridge.txt", mode="rb")
    fillying_bytes = stream.readinto(number_of_bytes)
    print(f"fillying bytes: {fillying_bytes}")
    print(f"number of bytes: {number_of_bytes}")
    stream.close()
except IOError as i:
    print("Something was really bad:", strerror(i.errno))

'''5. write(string) only to text files'''
author_london_bridge = "Louis-Ferdinand Céline, Dominic Di Bernardi"
try:
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/london bridge.txt", mode="at", encoding="utf-8")
    writing = stream.write("\nWritten by: " + author_london_bridge)
    print(f"number of characters written: {writing}")
    stream.close()
except IOError as i:
    print("Something happend by writting on the file:", strerror(i.errno))

'''6. write(bytearray) only for byte files'''
amorphous_data = bytearray(20)

for i in range(len(amorphous_data)):
    amorphous_data[i] = i

# the asignation below will complete but the last value will be replaced
# because of the size is only of 20 
amorphous_data[-1] = 21

try:
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/binFile.bin", mode="wb")
    stream = open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/binFile.bin", mode="wb")
    bytes_written = stream.write(amorphous_data)
    print(f"bytes written succesfully: {bytes_written}")
    stream.close()
except IOError as i:
    print("The bin file wasn't write succesfully:", strerror(i.errno))

'''7. open()'''
try:
    for line in open(file="C:/PCEP-And-PCAP-Python/PCAP/Module4/3_working with text and binary files/binFile.bin", mode="rb"):
        print(line)
        for character in line:
            print(character)
except IOError as i:
    print("Something failed:", strerror(i.errno))