# 不带参数的装饰器:(装饰器,被装饰函数都不带参数)
import time


def showtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("spend is {}".format(end_time - start_time))

    return wrapper


@showtime  # 这个@showtime相当于是 省略了写这一步代码：foo = showtime(foo)
def foo():
    print("我正在测试装饰器功能")
    time.sleep(3)


@showtime  # 这个@showtime相当于是 省略了写这一步代码：doo = showtime(doo)
def doo():
    print("这是doo函数")
    time.sleep(2)


foo()
doo()
