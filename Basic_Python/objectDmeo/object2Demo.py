"""
https://www.runoob.com/python/python-object.html
在python中继承中的一些特点：
1、如果在子类中需要父类的构造方法就需要显式的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看： python 子类继承父类构造函数说明。
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
语法：
派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
class SubClassName (ParentClass1[, ParentClass2, ...]):
"""


class Parent:  # 定义父类
    # 这是类变量
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')


c = Child()      # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod() # 调用父类方法
c.setAttr(200)   # 再次调用父类的方法 - 设置属性值
c.getAttr()      # 再次调用父类的方法 -

"""
你可以继承多个类
class A:        # 定义类 A
.....
class B:         # 定义类 B
.....
class C(A, B):   # 继承类 A 和 B
.....
你可以使用issubclass()或者isinstance()方法来检测。
issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。
"""

"""
方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：
"""

print("-----------------------------------风险--------------------------------")
class Parent1:  # 定义父类
    def myMethod(self):
        print('调用父类方法')



class Child1(Parent1):  # 定义子类
    def myMethod(self):
        print('调用子类方法')



c1 = Child1()  # 子类实例
c1.myMethod()  # 子类调用重写方法




















