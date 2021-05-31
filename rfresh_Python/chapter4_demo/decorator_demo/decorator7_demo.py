# author ：wang123 
# 创建时间 ：2021/2/10 15:45

# 不想要改变原有函数的功能，只想要添加新的功能，可以新定义一个新函数，嵌套原有的函数


def getInfo(func):
	def wrapper(*args, **kwargs):
		print("《Python自动化测试实战》")
		func()

	return wrapper


@getInfo
def f1():
	print("网易云课堂")


@getInfo
def f2():
	print("51CTO的平台")


# f1=wrapper  f2=wrapper
f1()
f2()
