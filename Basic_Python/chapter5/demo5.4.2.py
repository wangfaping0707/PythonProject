# status = input("请输入状态：")
#
# status = "奋斗中的小强！" if status.endswith("成功") else "失败"

name = input("What's your name:")
if name.endswith('Gumby'):
    print('Hello,', name)
elif name.endswith("wumeifang"):
    print("MyLover:", name)
elif name.endswith("lol"):
    print("I like this game:", name)
else:
    print("I dont't know you")
