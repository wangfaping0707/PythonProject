class Student:
    name = input("请输入你的姓名：")
    age = input("请输入你的年龄：")

    def print_file(self):
        print("name:" + self.name)
        print("age:" + str(self.age))

        # 构造函数
    def __init__(self):
        print("正在调用类的构造函数")


s1 = Student()
s1.print_file()
s1.__init__()
