# In the oop in python, every variable and function is regarded as an attribute.
# Python is a dynamic language, it can bind with these attributes any time

from types import MethodType


class foo1:
    def __init__(self,var1):
        self.var1 = var1


a = foo1(1)
print(a.var1)  # print 1
# Bind an variable with an instance a
a.var2 = 3
print(a.var2)  # print 3


def foo1_method(self):
    print('Dynamic language is good')


# Bind the foo1_method with an instance a
a.method = MethodType(foo1_method,a)
a.method()  # print
b = foo1(2)
# b.method()
# The above statement will report an error because the method 'method' just bind with a

# Bind 'foo1_method' with the class foo1, after binding, every instance of foo1 can use it
foo1.foo1_method = foo1_method
b.foo1_method() # print


# The keyword '__slots__' will restrict the attributes that foo2 have(including variables and methods)
class foo2:
    __slots__ = 'var1'

    def __init__(self,var1):
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
    def var1(self,val):
        self._var1 = val

    @property
    def var2(self):
        return 123


d = foo3()
d.var1 = 3
print(format('var1: %d, var2: %d') % (d.var1,d.var2))
