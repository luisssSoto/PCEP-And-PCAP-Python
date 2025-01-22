"""system() function"""
import os

os.system("pwd")
os.system("cd C:\\PCEP-And-PCAP-Python\\PCAP\\Module4")
os.system("pwd")
os.system("mkdir my-first-directory")
returned_value = os.system("rmdir my-first-directory")
os.system("mkdir my-first-directory")
print(os.system("dir"))

print(returned_value)
