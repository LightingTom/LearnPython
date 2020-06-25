#返回函数中，千万不能用循环中的变量，否则会出现闭包问题
#闭包问题反例：
#def count():
    # fs = []
    # for i in range(1, 4):
    #     def f():
    #          return i*i
    #     fs.append(f)
    # return fs
# f1, f2, f3 = count()
#这里f1(),f2(),f3()的值都为9，而不是1，4，9
#因为返回的函数只有在被调用的时候才会执行，这里第10行执行完这三个函数并没有执行，你call的时候才执行，所以这里内部变量i已经变成3，这三个函数都return 3*3

#这个方法中，arr是一个list，一个地址，所以arr的值变当且仅当这个函数被执行，就是call一次变一次
def createCounter():
    arr = [0]
    def count():
        arr[0] += 1
        return arr[0]
    return count


cntA = createCounter()
print(cntA(),cntA(),cntA())