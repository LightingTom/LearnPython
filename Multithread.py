import time, threading


# 新线程执行的代码:
# threading.current_thread() will return an instance for the current thread
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

import threading

# 假定这是你的银行存款:
balance = 0
# The modification for the global variables must acquire a lock
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


# If no lock, the result won't be zero
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            # After acquiring the lock, we can make sure the threads won't interrupt each other
            change_it(n)
        finally:
            # Be sure to release the lock
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# Every thread should use its local variables, but it can be hard to pass the variable between threads
# So, we can use a global dict to store the objects with thread as key
# The method threading.local() help us do this
# Solve the problem to exchange variables between the functions in one thread
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()