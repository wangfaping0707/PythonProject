# while 循环
# x = 1
# while x <= 10:
#     print(x)
#     x += 1

name = ''
while not name:
    name = input('Please enter your name:')
print('打印方式一：',"hello,{}！".format(name))
print('打印方式二：',"hello,%s！" % name)


eee = "3333"