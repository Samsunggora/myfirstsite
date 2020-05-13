# class Critter(object):  # class header
#     '''
#     vitrual animal
#     '''
#
#     def talk(self):  # class method
#         print('hello I am animal')
# crit = Critter()
# crit.talk()

# class Animal(object):
#     '''virtual animal'''
#
#     def __init__(self, name):
#         print ('init new animal')
#         self.name = name
#
#     def talk(self):
#         print ('hello ', 'my name is ', self.name)
#
#
# crit1 = Animal('bobik.')
# crit1.talk()

# class Menu(object):
#     def __init__(self, first, second, salt, water, candy):
#         print('Class for make menu on all happening')
#         self.first = first
#         self.second = second
#         self.salt = salt
#         self.water = water
#         self.candy = candy
#
#     def show(self):
#         print(self.first, self.second, self.salt, self.water, self.candy)
#
#
# first_holiday = Menu("self", 'pure', 'olive', 'kompot', 'ice cream')
# first_holiday.show()

class Bulding(object):
    def __int__(self, first, second, trith, fourth):
        print('make item')
        self.first = first
        self.second = second
        self.trith = trith
        self.fourth = fourth

    def bild(self):
        print('first bilding', self.first)
        print('second bilding', self.second)
        print('trith bilding', self.trith)
        print('fourth bilding', self.fourth)


x = Bulding()
x.bild()
