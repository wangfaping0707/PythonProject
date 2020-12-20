# 这是一个判断用户登录的实例
account = "王发平"
password = "123456"

user_name = input("请输入用户名;")
if user_name == account:
    print("------用户名正确------")
    user_password = input("请输入密码")
    if user_password == password:
        print("密码正确")
        print("恭喜你,登陆成功")
    else:
        print("密码错误,请重新登录")
else:
    print("用户名输入错误，请重新输入，小崽子")
