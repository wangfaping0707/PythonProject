"""
python-map的用法:  map()函数
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
map() 函数语法：map(function, iterable, ...)
参数:  function -- 函数   iterable -- 一个或多个序列
注意：map()函数不改变原有的 list，而是返回一个新的 list。
"""
# 当seq只有一个时，将函数func作用于这个seq的每个元素上，并得到一个新的seq。
# 以下实例展示了 map() 的使用方法：

list_x = [1, 2, 3, 4, 5, 6]


def square(x):      # 计算平方数
    return x * x


re = map(square, list_x)    # re是一个对象，需要把它转为1列表
list_y = list(re)
print("平方之后的列表值：", list_y)

"""
利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。
由于list包含的元素可以是任何类型，因此，map() 不仅仅可以处理只包含数值的 list，
事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。
假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，
把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
"""
names = ['adam', 'LISA', 'barT']   # 期望转换后的输出：['Adam','Lisa','Bart']


def format_name(s):
    s1 = s[0:1].upper() + s[1:].lower()
    return s1


s2 = map(format_name, names)
print("姓名转换后的名字：", list(s2))

# 用lambda表达式来使用map
result = map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(list(result))

# 提供了两个列表，对相同位置的列表数据进行相加, 当seq（序列）多于一个时，map可以并行（注意是并行）地对每个seq执行如下图所示的过程：
# python3中可以处理类表长度不一致的情况，但无法处理类型不一致的情况，
L1 = [1, 3, 5, 7, 9, 20, 40]
L2 = [2, 4, 6, 8, 10, 25]
result2 = map(lambda x, y: x + y, L1, L2)
print("使用lambda表达式的运行结果：", list(result2))


# python3中可以处理类表长度不一致的情况，但无法处理类型不一致的情况，
l4 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2])
print("l4的类型是：", l4)
for i in l4:
    print(i)

# l4 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 'a'])
# for i in l4:
#     print(i)


# 特殊用法，做类型转换：
T = map(int, '1234')
for i in T:
    print(type(i))
    print(i)

