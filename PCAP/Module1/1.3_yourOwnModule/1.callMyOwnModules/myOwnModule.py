print('I like to be a "module"')

'''__name__variable says the name of the file that is being executed:
for instance; if you run this file just here, the variable name will keep
the value "__main__" but if you import this file like a module and run it
from that file, the value is going to be "nameOfModule" '''
print(__name__)

'''So that if you want to know the context where your code was executed, this is 
a way that you can take:'''
if __name__ == "__main__":
    print("From module")
else: 
    print("From other file")
