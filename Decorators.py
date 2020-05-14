class Animal(object):
    def __init__(self, name):
        """show opportunity"""
        print('make new class')
        self.__name = name
    @property
    def name(self):
        return self.__name


