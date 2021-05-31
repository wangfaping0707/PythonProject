# 如果要使用一个except字句捕获多种异常。可在一个元组中指定这些异常

try:
    x = int(input("请输入第一个参数："))
    y = int(input("请输入第二个参数："))
    print(x / y)
except (ZeroDivisionError,TypeError,ValueError) as e:
    print("YOURS numbers were bogus ....")
    print(e)