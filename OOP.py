# In the oop in python, every variable and function is regarded as an attribute.
# Python is a dynamic language, it can bind with these attributes any time

from types import MethodType


class foo1:
    def __init__(self, var1):
        self.var1 = var1


a = foo1(1)
print(a.var1)  # print 1
# Bind an variable with an instance a
a.var2 = 3
print(a.var2)  # print 3


def foo1_method(self):
    print('Dynamic language is good')


# Bind the foo1_method with an instance a
a.method = MethodType(foo1_method, a)
a.method()  # print
b = foo1(2)
# b.method()
# The above statement will report an error because the method 'method' just bind with a

# Bind 'foo1_method' with the class foo1, after binding, every instance of foo1 can use it
foo1.foo1_method = foo1_method
b.foo1_method()  # print


# The keyword '__slots__' will restrict the attributes that foo2 have(including variables and methods)
class foo2:
    __slots__ = 'var1'

    def __init__(self, var1):
        self.var1 = var1


c = foo2(3)


# it will report an error if bind other attributes(like shown below)
# c.var2 = 4
# c.method = foo1_method (also not allowed)


# '@property' can specify the read and write property of attributes of a class
# Pay attention to the different between var, _var, __var
# var is a public variable
# _var is a special variable, means "I'm public but don't access me"
# __var is a private variable
# In '@property', we should use _var. If use var, self.var will be regarded as a function and it will cause a dead loop
class foo3:
    # '@property' equals to a getter method, and we can use a.var1 as get_var1()
    @property
    def var1(self):
        return self._var1

    @var1.setter
    def var1(self, val):
        self._var1 = val

    @property
    def var2(self):
        return 123


d = foo3()
d.var1 = 3
print(format('var1: %d, var2: %d') % (d.var1, d.var2))


# In python, there will be some custom class (定制类).
# It is like implementation of some built-in method for the class Object in Java
class Student:
    def __init__(self, name, id, score):
        self.name = name
        self.id = id
        self.score = score

    # Like the toString() method
    def __str__(self):
        return format('Name: %s\nID: %s\nScore: %d') % (self.name, self.id, self.score)

    # __repr__ is used in command line of python, shown to the developer, and __str__ is shown to the user
    __repr__ = __str__


print(Student('Tom', '11813015', 100))


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

# Used to implement the iterator
    def __iter__(self):
        return self

# Used to implement the iterator
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

# Implement the method get(i) like the list and the slice function
    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for i in range(n):
                a,b = b, a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print(Fib().__getitem__(5))
print(Fib()[:5])

class Integer:
    def __init__(self, n):
        if not isinstance(n,int):
            raise TypeError('Required int')
        self.n = n

    # Once implement __call__, the instance can be called as a function
    def __call__(self):
        print('value:',self.n)


e = Integer(2)
e()
