# author ：wang123 
# 创建时间 ：2021/1/12 23:39
"""
Python 列表推导式
列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。
它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是 0 个或多个 for 或者 if 语句。
那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，
在这个以 if 和 for 语句为上下文的表达式运行完成之后产生。
列表推导式的执行顺序：各语句之间是嵌套关系，左边第二个语句是最外层，依次往右进一层，左边第一条语句是最后一层。

1.列表推导式书写形式：
[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]

"""

list_test = [x * y for x in range(0, 7) if x > 3 for y in range(2, 6)]

print(list_test)

"""
他的执行顺序是:
for x in range(1,5)
    if x > 2
        for y in range(1,4)
            if y < 3
                x*y
"""

dict1 = {"name": "wuya", "age": 18, "sex": "male"}

dict2 = dict1.copy()

print("打印dict2：", dict2)

list_test1=dict1.keys()

print(list_test1)

print(dict2.values())

for key in dict1.keys():
	print(key, ":", dict1.get(key))

print(dict1.items())

for key, value in dict2.items():
	print(key, "->", value)
