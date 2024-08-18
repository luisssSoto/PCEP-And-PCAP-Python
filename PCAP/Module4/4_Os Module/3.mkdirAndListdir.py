"""mkdir and listdir"""
'''mkdir creates a new directory but if this has been created before
will be an error'''
'''listdir allows us to see all the content in the current directory'''

import os

# Relative or absolute path
# mode setting the rights of access
try:
    os.mkdir(path="C:/pcep-and-pcap-python/pcap/Module4/4_Os Module/my_first_directory",mode=511)
except FileExistsError as e:
    print(e.args)
    print(os.listdir(path="C:/pcep-and-pcap-python/pcap/Module4/4_Os Module"))


#setting rights of access with os.chmod() function 
