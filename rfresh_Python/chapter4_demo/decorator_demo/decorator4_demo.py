import time


# 带参数的被装饰的函数


def showtime(func):
    def wrapper(a, b):
        start_time = time.time()
        func(a,b)
        end_time = time.time()
        print("执行这个函数所需要的时间是：", (end_time - start_time))

    return wrapper


@showtime
def add(a, b):
    print("计算加法：", (a + b))
    time.sleep(3)


@showtime
def sub(a, b):
    print("计算减法：", (a - b))
    time.sleep(2)


add(2, 5)
sub(9, 1)
