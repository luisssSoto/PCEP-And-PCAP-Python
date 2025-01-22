"""getcwd() method"""
'''it returns the absolute route which we are currently'''

import os

os.makedirs("C:/pcep-and-pcap-python/pcap/Module4/4_Os Module/my_first_directory/my_second_directory")
os.chdir("C:/pcep-and-pcap-python/pcap/Module4/4_Os Module/my_first_directory")
print(os.getcwd())
os.chdir("C:/pcep-and-pcap-python/pcap/Module4/4_Os Module/my_first_directory/my_second_directory")
print(os.getcwd())