from functools import reduce

# 连续计算。连续调用lambad


list_x = ['1', '2', '3', '4', '5', '6', '7']
result = reduce(lambda x, y: x + y, list_x, "ab")
print("打印result结果：", result)

list_y = [1, 2, 3, 4, 5, 6, 7]
result1 = reduce(lambda x, y: x + y, list_y, 10)
print("打印result1结果：", result1)


def add(x, y):  # 两数相加
    return x + y


sum1 = reduce(add, [1, 2, 3, 4, 5])  # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)


