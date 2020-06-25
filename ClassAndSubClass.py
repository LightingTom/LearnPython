# The prefix "__" means private
# The type of the method of a instance is method, the type of the method of a class is function
# see type(animal.run) and type(animal('hhh').run)
# The function like __xx__ can be "override"
# For example, if override __len__() for animal, we can use len(animal)


class Student:
    def __init__(self, name, id, score):
        self.__name = name
        self.__id = int(id)
        self.__score = int(score)

    def showInfo(self):
        print(format('Name: %s\nStudentID: %d\nScore: %d')%(self.__name, self.__id, self.__score))

    def lower(self):
        self.__name = str.lower(self.__name)

    def __len__(self):
        return 1


a = Student('Tom','11813015','100')
a.showInfo()
print(format("a's length is %d") % len(a))


class animal(object):
    def __init__(self,intro):
        self.__intro = intro

    def move(self):
        print('animal is running')

    def introduce(self):
        print(format('My name is %s, my color is %s') % (self.__class__.__name__, self.__intro))

class dog(animal):
    def move(self):
        print('dog is running')

    def eat(self):
        print('Dog eat meat')


class rabbit(animal):
    def move(self):
        print('rabbit is jumping')

    def eat(self):
        print('rabbit eat grass')


b = animal('Black and white')
b.introduce()
b.move()
c = dog('Yellow')
c.introduce()
c.move()
c.eat()
d = rabbit('white')
d.introduce()
d.move()
d.eat()


class Runnable(object):
    def run(self):
        print(self.__class__.__name__, 'is running')


class Flyable(object):
    def fly(self):
        print (self.__class__.__name__, 'is flying')


# Python also allowed multiple inheritance, it can be write like this
# What's more, the name of runnable and flyable should be RunnableMixIn and FlyableMixIn
# In this way, we can better understand the direct inheritance chain for Bird and Cat
# MixIn means the additional function
class Bird(animal,Flyable):
    pass


class Cat(animal,Runnable):
    pass


e = Bird('Green, Red, Yellow')
f = Cat('Black')
e.fly()
e.introduce()
f.run()
f.introduce()
