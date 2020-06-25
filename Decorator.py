import time
import math


# The decorator
# Usually, the name for function a is wrapper.
# The decorator must return the same thing as the original function and have the same argument.
def display_time(func):
    def a(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("Run time: ", t2 - t1)
        return result

    return a


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


@display_time # Call the decorator
def count_prime(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count = count + 1
    return count


print(count_prime(10000))
