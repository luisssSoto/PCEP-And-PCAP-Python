""" PyPI (Python Package Index) is a repository where the
most important packages of Python are saved, while "pip"
is the main tool to import this packages to our proyect,
althought isn't have any cost to import any packages
frome PyPI, you MUST follow the license terms about that
package """

''' The command to know if you have the tool "pip" is 
"pip --version" in Linux you need to use a package 
management to install pip if it's not in your system'''

''' pip support us to avoid the "dependency heal" which 
happens when one package depends to other one, and this
one to other one and so on, so pip install all the 
dependencies that 1 package could have instead to 
install manualy each of this one '''

''' To ask for help, only type "pip help", remember that
if you have linus maybe the command could be just like
this: "pip3 help", pip help show us the operations that
"pip" can use '''

''' if you wanna know more about one specific command of pip
"pip help operation" for example this: "pip help install" to know more
about the install operation'''

''' "pip list" is used to know the packages you've already installed, you
probably have installed the "pip" and "setuptools'''

''' "pip show packageName" is for get more details about the package you've
gotten installed before, for instance "pip show pip" there two fields you 
should know when we use this command:
Requires: Which packages are needed to use packageName successfully
Required-by: Which packages needs that packageName will be executed successfully'''

''' "pip search whatAreYouLookingForward" is used to search at PyPI for some
packages 
Note: this is not available currently'''

''' admin: "pip install packageName"
    not admin: "pip install --user packageName", try it 
    whit "pygame" package '''

''' "pip install -U packageName": uptading the package to
its newest version 
Note: here also will be applyed the admin and not admin
mode'''

''' "pip install packageName == packageVersion" you can choose
the version you want '''

''' "pip uninstall packageName" will be uninstall the package '''
