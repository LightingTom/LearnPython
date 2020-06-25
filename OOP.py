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
