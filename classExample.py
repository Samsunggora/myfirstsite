# class Critter(object):  # class header
#     '''
#     vitrual animal
#     '''
#
#     def talk(self):  # class method
#         print('hello I am animal')
# crit = Critter()
# crit.talk()

class Animal(object):
    '''virtual animal'''

    def __init__(self, name):
        print ('init new animal')
        self.name = name

    def talk(self):
        print ('hello ','my name is ', self.name)


crit1 = Animal('bobik.')
crit1.talk()
