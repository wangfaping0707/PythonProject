# author ：wang123 
# 创建时间 ：2021/2/2 23:37


def f():
	name = "我是父函数的值"

	def f1():
		name = "我是子函数的值"
		print(name)
	return f1()


a = divmod(100, 3)
print(a)

