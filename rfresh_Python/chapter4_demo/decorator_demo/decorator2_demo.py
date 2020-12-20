"""
闭包用途:
3.1 装饰器！装饰器是做什么的？其中一个应用就是，我们工作中写了一个登录功能，我们想统计这个功能执行花了多长时间，
我们可以用装饰器装饰这个登录模块，装饰器帮我们完成登录函数执行之前和之后取时间。
"""
import time

# 装饰器的原型


def foo():
    print("foo....")
    time.sleep(3)


def showtime(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper


foo = showtime(foo)
foo()
