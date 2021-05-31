"""
self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:
"""


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
