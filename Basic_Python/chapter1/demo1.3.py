print(bool(3))
print(bool(0))
# type()函数用来查看类型
print(type(bool(0)))

# Python变量使用前必须赋值，因为Python变量没有默认值
# 在Python中，名称(标识符)只能由字母、数字和下划线(_)构成，且不能以数字打头
# 因此Plan9是合法的变量名，而9Plan不是
i = 3
print("正在运算中：%f" % (i * 2))
# 函数input
# input("The meaning of life：")

x=input("x:")
y=input("y:")
print(int(x)*int(y))


