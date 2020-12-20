from People_Demo import Human


class Student(Human):
    # sum = 0
    #
    def __init__(self, school, name, age):
        self.school = school
        # 调用父类构造方法  方式一
        # Human.__init__(self,name,age)

        # 调用父类构造器方法  方式二
        super(Student, self).__init__(name, age)

        # self.name = name
        # self.age = age
        self.__score = 0
        self.__class__.sum += 1

    def do_homework(self):
        print("This is a subclass method,English homework")
        super(Student,self).do_homework()
        # super(Student,self).get_name()


s1 = Student("红十字会中学", "徐岚", 19)
print("通过对象访问：", s1.sum)
print("通过类名访问：", Student.sum)
print("对象的名字：", s1.name)
print("对象的年龄：", s1.age)
print("---------------分割线--------------------")
s1.do_homework()
