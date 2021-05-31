"""
Python 子类继承父类构造函数说明:
如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。
子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。
"""


class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('name:%s  age:%d' % (self.name, self.age))
        print("我是Father类-----------------------")

    def getName(self):
        return 'Father' + self.name
