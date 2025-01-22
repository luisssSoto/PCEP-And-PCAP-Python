"""makedirs and chdir"""

import os

try:
    os.makedirs("C:/pcep-and-pcap-python/pcap/Module4/4_Os Module/my_first_directory/my_second_directory")
    os.chdir(path="C:/pcep-and-pcap-python/pcap/Module4/4_Os Module/my_first_directory/")
    print(os.listdir())
except FileExistsError as e:
    print(e)