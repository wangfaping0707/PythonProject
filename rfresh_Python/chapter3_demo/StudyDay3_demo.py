"""
Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
注意：在 Python3.x 中 raw_input() 和 input() 进行了整合，去除了 raw_input( )，
仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
"""

a = input("请输入内容：")

print("a的值是：", a)
print(type(a))

a = int(a)

if a == 1:
    print("apple")
elif a == 2:
    print("orange")
elif a == 3:
    print("banana")
else:
    print("shopping")
