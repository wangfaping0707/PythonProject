"""
如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__，语法格式如下：
"""
from object1_demo import *


class Son1(Father):
    def __init__(self, name,age,favorite):
        # 如果显示调用父类的构造方法,那么此时son1对象就有了从父类继承过来的name和age属性
        super().__init__(name,age)
        self.name = name
        self.age = age
        self.favorite = favorite
        print("Hi,I'm lonely")

    def getPersonInfo(self):
        print("大家好，正在获取此人的信息")
        return '此人的兴趣爱好是:%s' % self.favorite

    def getFullInfo(self):

        print("获取完整个人信息：%s%s%d" % (self.favorite, self.name, self.age))

"""
如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
super(子类，self).__init__(参数1，参数2，....)
还有一种经典写法：
父类名称.__init__(self,参数1，参数2，...)"""

# s1 = Son1('钓鱼')
# print("------------------------------------------")
# print(s1.getPersonInfo())
s2 = Son1('司马相如',27,'读书')
print(s2.__dict__)
s2.getFullInfo()


"""
学习笔记：
情况一：子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
情况二：子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
情况三：子类重写__init__()方法又需要调用父类的方法：使用super关键词：
super(子类，self).__init__(参数1，参数2，....)
class Son(Father):
  def __init__(self, name):   
    super(Son, self).__init__(name)

"""





















