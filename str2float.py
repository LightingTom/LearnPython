from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(c):
    return DIGITS[c]


def str2float(s):
    def f(x, y):
        return 10 * x + y

    def g(x, y):
        return x / 10 + y

    front = s[0:str.find(s, '.')]
    rear = s[:str.rfind(s, '.'):-1]

    result = reduce(f, map(char2num, front))
    result += reduce(g, [data / 10 for data in map(char2num, rear)])
    return result


str2float('123.345')
