def fib_generator(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield a
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == '__main__':
    f = fib_generator(8)
    i = 0
    for i in range(10):
        print(next(f))
        i = i+1
