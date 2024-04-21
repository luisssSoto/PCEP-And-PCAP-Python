import myOwnModule

"""Once we confirm that our tests have done successfully,
we can use this functions"""
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(myOwnModule.suml(zeroes))
print(myOwnModule.prodl(ones))


"""We've been supposed that we work with the files (module
and main) in the same path, but we're going to move the
module file in order to put it in another directory, to
access to it"""

'''So that, there is a list calls "path" that keeps inside
it all the paths, the only thing you need to do is to add
the path which finds the module which you want to import
and python will search for the list from the beginning and
if find it the importation will be succesfully, if not the 
importation will be failed '''
import sys

for p in sys.path:
    print(p)

#you can use a relative path, but be careful
sys.path.append("C:\\PCEP-Certified-Entry-Level-Python-Programmer-\\PCAP\\Module1\\1.32_yourOwnModule")
import myOwnModule2

print(sys.path)
