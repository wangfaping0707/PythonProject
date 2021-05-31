# author ：wang123 
# 创建时间 ：2021/2/10 17:48


def login(func):
	def wrapper(token):
		if token == "abc123":
			func(token)
		else:
			print("请登录系统")

	return wrapper


@login
def profile(token):
	print("欢迎获取主页信息")


profile("abc1230")
