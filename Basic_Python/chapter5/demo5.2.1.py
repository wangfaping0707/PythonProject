# 可同时(并行)给多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)
# 使用这种方式还可以同时交换多个变量的值
x, y = z, x
print(x, y, z)

values = 1, 2, 3, 4, 5
print(values)
c, d, e, f, g = values
print(c, d, e, f, g)

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key)
print(value)

a, b, *rest = [1, 2, 3, 4, 5, 6]
print(a, b)
print(rest)

name = 'Albus Percival Wulfric Brian Dumbledore'
first, *middle, last = name.split()
print(middle)
print(type(middle))
print(type(last))

print("验证True和False代表的数学值：", True + False + 21)
print(bool("I think,therefore I am"))
print(bool(42))
print(bool(0))
