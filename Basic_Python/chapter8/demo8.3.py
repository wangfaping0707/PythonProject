"""
使用try/except语句来捕获异常，并进行处理
input函数是python中内置的函数，其输出的结果是一个字符串，如果要用于计算，需要将其转成数字
"""

try:
    x = int(input("请输入第一个参数："))
    print("x的类型是：", type(x))
    y = int(input("请输入第二个参数："))
    # y = input()
    print("y的类型是：", type(y))
    result = x / y
    print("result的类型是：", type(result))
    print("输出计算结果", result)
except ZeroDivisionError:
    print("除法中第二个参数不可为零")
except TypeError:
    print("That wasn't a number, was it ?")
