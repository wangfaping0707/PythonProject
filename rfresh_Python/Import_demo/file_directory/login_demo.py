# author ：wang123 
# 创建时间 ：2021/2/1 21:34


def login():
	username = input("请输入用户名：")
	password = input("请输入密码：")
	if username == "wuya" and password == "admin":
		return "adcde345rfwerk565ger56500"


def profile(session):
	if session == login():
		print("欢迎您访问无涯个人主页")
	else:
		print("您未登录系统，跳转到登录页，302")


profile("adcde345rfwerk565ger56500")

