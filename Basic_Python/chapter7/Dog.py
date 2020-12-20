class Dog:
    name = "藏獒"  # 类变量
    age = 0  # 类变量
    hobby = '打球'
    color = "Blue"
    sum = 0

    # 类变量  实例变量
    def __init__(self, name, age, hobby):
        # 构造函数，创建对象并初始化对象的属性
        self.name = name  # 实例变量
        self.age = age  # 实例变量
        self.hobby = hobby  # 实例变量
        self.__color = "蓝色"
        self.__class__.sum += 1
        print("当前的小狗数量为：" + str(self.__class__.sum))

    def homework(self):
        print("do homework............")
        print("这是实例变量：", self.name)
        print("这是类变量：", Dog.name)

    def eating(self, food):
        self.food = food
        print(self.name + "同学爱吃：" + self.food)

    # Python中定义 类方法 需要使用装饰器 classmethod 将方法标识出来且方法中的默认参数名称为cls
    # 决定一个方法是类方法还是实例方法的根本原因在于我们是否在这个方法上面增加了一个装饰器
    @classmethod
    def plus_sum(cls):
        # cls.sum += 1
        print("在类方法中，访问当前的小狗数量:" + str(cls.sum))
        print("类方法被调用。。。。。。。。。。。。。")

    # Python 中的静态方法使用装饰器 staticmethond 标识出来,静态方法是可以同时被类和对象调用的
    @staticmethod
    def add(x, y):
        print('This is a static method!')
        print(Dog.hobby)
        print()
        pass


# Python的内置变量“_dict_".它保存的是当前对象下面所有的相关变量
d1 = Dog("哈士奇", 2, '啃骨头。。。')
d1.homework()
d1.add(1, 2)
# print("----------------------------------------------------------")
# d2 = Dog("阿拉斯加", 3, "gd")
# d2.homework()
# print("----------------------------------------------------------")
# d3 = Dog("狮子狗。", 7, "白色毛发")
# d3.homework()
print("*****************************************************")
# Dog.plus_sum()

# 打印 d1 对象的变量
# print(d1.__dict__)

# 打印 当前类的变量
# print(Dog.__dict__)

d4 = Dog("中华田园犬", 3, "傲娇")
d4.eating("肉骨头。。。。")
d4.__color = "彩虹色"
print(d4.__color)
# d4对象所拥有的变量
print(d4.__dict__)

d5 = Dog("日本秋田犬", 17, "甜蜜蜜")
# print(d5.__color)


print("--------------------------------------------------")
print(Dog.plus_sum())
