from objectDmeo.object1_demo import *

"""
如果在子类中需要父类的构造方法就需要显式地调用父类的构造方法，或者不重写父类的构造方法。
子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__。"""


class Son(Father):
    def getName(self):
        return 'Son.name:%s  Son.age:%d' % (self.name, self.age)


s = Son('成翠红', 33)
# 显示调用父类的getName方法
print(s.getName())
