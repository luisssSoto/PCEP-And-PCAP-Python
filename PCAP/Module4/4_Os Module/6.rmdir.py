"""rmdir() and removedirs() functions"""
import os

'''rmdir()'''
os.makedirs("./PCAP/Module4/4_Os Module/my-first-directory")
print(os.listdir(path="./PCAP/Module4/4_Os Module/"))
os.rmdir("PCAP/Module4/4_Os Module/my-first-directory")
print(os.listdir(path="./PCAP/Module4/4_Os Module/"))

'''removedirs()'''
os.makedirs("PCAP/Module4/4_Os Module/my-first-directory/my-second-one")
os.chdir("PCAP/Module4/4_Os Module/")
print(os.listdir())
os.removedirs("my-first-directory/my-second-one")
print(os.listdir())
