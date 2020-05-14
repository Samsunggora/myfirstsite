# class Incapsul(object):
#     """This class exampling incapsuling"""
#
#     def __init__(self, name, hide):
#         print('add new class')
#         self.name = name
#         self.__hide = hide
#
#     def names(self):
#         print ('My name is:', self.name)
#         print ('My hide name is:', self.__hide)
#
#
# x = Incapsul('name', 'hiden')
# x.names()
class Example(object):
    """Rundom comment"""

    def __init__(self, name, hide):
        print('add new class')
        self.name = name
        self.__hide = hide

    def names(self):
        print ('My name is:', self.name)
        print ('My hide name is:', self.__hide)

    def __private(selfs):
        print('This is hidden method')

    def publick(self):
        print('This is open method')

x = Example
