from rfresh_Python.chapter3_demo.ExtendsTest import Human


class Student(Human):

    # sum = 0

    # python中的构造函数

    def __init__(self, name, age, college):
        self.college = college
        # 子类构造器中显式父类构造器 方式一
        # Human.__init__(self, name, age)

        # 子类调用父类构造器方式二
        super(Student, self).__init__(name, age)

        # self.__score = 0
        # # self.__class__.sum +=1
        # # print("当前班级学生总数为：",self.__class__.sum)

    def print_file(self):
        print("name是：", self.name)
        print("age的值是：", self.age)

    def do_homework(self):
        print("请及时做家庭作业")
        print("调用这个方法的对象名称：", self.name)
        print("调用这个方法的对象年龄", self.age)
        super(Student, self).do_homework()

    def marking(self, score):
        self.__score = score
        print(self.name + "本次考试的成绩为:" + str(self.__score))

    @classmethod
    def plus_num(cls):
        cls.sum += 1
        print("当期班级学生总人数和：" + str(cls.sum))

    @staticmethod
    def add(x, y):
        print(x + y)
        print("静态方法是否可以访问类变量：", Student.sum)
        print("This is a static method")


# s1 = Student("冷小寒", 17)
# # Student.plus_num()
# # s2 = Student("冷小筱", 17)
# # Student.plus_num()
# # s3= Student("冷小玲", 17)
# # Student.plus_num()
# #
# # Student.add(3,7)

s4 = Student("宫晓婷",19,"浙江大学")
s4.marking(149)
s4.__score = 198
s4.loving = "游泳"
# s4.name = "王晓静"
print(s4.__dict__)

s5 = Student("冯小兰", 21,"浙江中医药大学")
print(s5.sum)
print(Student.sum)
print(s5.name)
print(s5.age)
s5.get_name()
s5.do_homework()
