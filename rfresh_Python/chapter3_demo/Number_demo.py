a = 1
print("a的数据类型是：", type(a))

b = 3.1415932

print("b的数据类型是：", type(b))

c = a + b

print("c的数据类型是：", type(c))

# python中除法 / 得到的结果位float类型
# Python中除法 // 得到的结果位int类型

print("结果类型：", type(2 / 2))
print("结果类型：", type(2 // 2))

if 2 > 1:
    print('2 > 1 is true')
else:
    print('2 > 1 is false')
print('Program is end')
