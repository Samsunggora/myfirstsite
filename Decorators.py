class Animal(object):
    def __init__(self, name):
        """show opportunity"""
        print('make new class')
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print('Error: Name is clear!')
        else:
            self.__name = new_name

    def talk(self):
        print('Hello my name is :', self.name)


x = Animal('barbos')
x.talk()
x.name = "pes"
print(x.name)
