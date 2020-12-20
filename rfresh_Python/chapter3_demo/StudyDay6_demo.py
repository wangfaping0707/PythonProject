# 函数的默认参数练习  必输参数   关键字参数  默认参数
def print_student_file(name, gender="女", age=18, college="百合花高中"):
    print("我叫" + name)
    print("我今年" + str(age) + "岁")
    print("我是" + gender + "生")
    print("我在" + college + "上学")


print_student_file("陈晓丽", "女", 17, "紫罗兰高中")
print_student_file("王可萌")
print_student_file("孙贝贝", age=16)
