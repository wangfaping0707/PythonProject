"""
Python3 filter() 函数:
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，
最后将返回 True 的元素放到新列表中。
以下是 filter() 方法的语法: filter(function, iterable)    function -- 判断函数   iterable -- 可迭代对象
返回值: 返回一个迭代器对象
"""

# 实例: 过滤出列表中的所有奇数：


def is_odd(n):
    return n % 2 == 1


result = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("返回过滤后的列表：", list(result))

result1 = filter(lambda x: True if x % 2 == 1 else False, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("打印result1的结果：", list(result1))

# 需求；过滤掉小写，只保留大写字母  Python提供了isupper()，islower()，istitle()方法用来判断字符串的大小写
list_word = ['s', 'S', 'd', 'F', 'L', 'S']

result2 = filter(lambda x: True if x.isupper() else False, list_word)
result3 = filter(lambda x: True if x.islower() else False, list_word)

print(list(result2))
print(list(result3))

