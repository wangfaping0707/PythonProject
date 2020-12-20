x = (1, 2, 3, 4, 5)
print(type(x))

# 只包含一个值的元组
y1 = (32)
print(type(y1))
y = (32,)
print(type(y))
y2 = ()
print(type(y2))

print(3 * (40 + 2))

print(3 * (40 + 2,))

# 函数tuple的工作原理与List很像：它将一个序列作为参数，并将其转换为元组，如果参数已经是元组，就原封不动的返回它
print(tuple("woaretheworld"))  # 参数为字符串
print(tuple([3, 1, 3, 5, 2, 4]))  # 参数为列表
