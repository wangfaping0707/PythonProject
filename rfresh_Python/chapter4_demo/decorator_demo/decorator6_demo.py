
import time
"""
类装饰器:一般依靠类内部的__call__方法
1、不带参数的类装饰器: 基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数
__init__ ：接收被装饰函数
__call__ ：实现装饰逻辑

2、带参数的类装饰器
带参数和不带参数的类装饰器有很大的不同
__init__ ：不再接收被装饰函数，而是接收传入参数
__call__ ：接收被装饰函数，实现装饰逻辑
"""


class Foo(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args, **kwargs)
        end_time = time.time()
        print("执行这个函数所需要的时间：", (end_time - start_time))


@Foo  # bar = Foo(bar)->命名一个变量bar,和函数同名的变量，然后 bar = Foo(add)  然后在bar()  也就是Foo(add)()
def add(a, b):
    print("执行add函数计算结果：", (a + b))
    time.sleep(3)


add(3, 4)
