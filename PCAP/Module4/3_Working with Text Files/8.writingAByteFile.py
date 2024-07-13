"""Writing a bin file"""
from os import strerror

amorphous_data = bytearray(10)

for i in range(len(amorphous_data)):
    amorphous_data[i] = 10 + i
    
print(amorphous_data)

try:
    stream = open(file='C:/Programming Languages/Python/PCEP-PCAP-Python/PCEP-PCAP/PCAP/Module4/3_Working with Text Files/fileBin.bin', mode='wb') #binary mode doesn't take an encoding argument
    writing = stream.write(amorphous_data)
    print(writing) # check if all the data was written succesfully
    stream.close()
except IOError as e:
    print('Something was wrong:', strerror(e.errno))

try:
    stream = open(file='C:/Programming Languages/Python/PCEP-PCAP-Python/PCEP-PCAP/PCAP/Module4/3_Working with Text Files/fileBin.bin', mode='rb')
    file = stream.read()
    for byte in file:
        print(byte, end=' ')
except IOError as e:
    print('Something was wrong:', strerror(e.errno))
    
'''Note:
The write() method returns the number of bytes successfully written.
If the values differ from the length of the method arguments, 
it may mean that there are some typing errors.'''