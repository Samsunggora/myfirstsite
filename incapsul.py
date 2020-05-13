class Incapsul(object):
    """This class exampling incapsuling"""

    def __init__(self, name, hide):
        print('add new post')
        self.name = name
        self.__hide = hide

    def names(self):
        print ('My name is:', self.name)
        print ('My hide name is:', self.__hide)


x = Incapsul('name', 'hiden')
print(x._Incapsul__hiden)
