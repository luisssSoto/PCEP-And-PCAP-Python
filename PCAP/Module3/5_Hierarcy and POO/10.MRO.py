"""MRO"""
'''It means the approach how to Python search in their own system of classes
according of the hierarchy and you must to follow this approach wheter you want
or not'''
class Top:
    def m_top(self):
        print('superior')
class Middle(Top):
    def m_middle(self):
        print('medio')
class Bottom(Middle):
    def m_bottom(self):
        print('abajo')
        
obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()

'''Altought the hierarchy below does not have
much sense, it is allowed'''
class Top:
    def m_top(self):
        print('superior')
class Middle(Top):
    def m_middle(self):
        print('medio')
class Bottom(Middle, Top):
    def m_bottom(self):
        print('abajo')
        
obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()

'''But if you try to do this method you'll get an
TypeError because of MRO that tries to search
the order of hierarchy from left to the right'''
class Top:
    def m_top(self):
        print('superior')
class Middle(Top):
    def m_middle(self):
        print('medio')
class Bottom(Top, Middle):
    def m_bottom(self):
        print('abajo')
        
obj = Bottom()
obj.m_bottom()
obj.m_middle()
obj.m_top()