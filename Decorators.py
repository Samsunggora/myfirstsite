class Animal(object):
    def __init__(self, name):
        """show opportunity"""
        print('make new class')
        self.__name = name
    @property
    def name(self):
        return self.__name
    def talk(self):
        print('Hello my name is :', self.name)

x = Animal('barbos')
x.talk()


