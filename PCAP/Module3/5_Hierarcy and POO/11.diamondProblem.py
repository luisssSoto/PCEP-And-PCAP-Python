"""Diamond Problem"""
'''The diamond problem comes when exist the multiple hierarchy and if it exist methods
which calls exactly like others methods which are in the classes at the exact level,
the methods could be overwritten each other'''

class Top:
    def m_top(self):
        print('m_top')
    def m_middle(self):
        print('m_middle_top')
class MiddleLeft(Top):
    def m_middle(self):
        print('m_middle_left')
class MiddleRight(Top):
    def m_middle(self):
        print('m_middle_right')
class Bottom(MiddleRight, MiddleLeft): # You can change the order of the classes to expect different response
    def m_bottom(self):
        print('m_bottom')
        
obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()

#Note: Remember the MRO always apply, try to apply change the parameters like this:
# and watch the TypeError (Top, Middle...)

