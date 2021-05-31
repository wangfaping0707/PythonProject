# author ：wang123 
# 创建时间 ：2021/1/31 23:22

# Python中的排序sorted(d.items(), key=lambda x: x[1])

# 1、Python中对键值对进行输出和排序
d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
# 以列表形式输出字典d的key
b1 = [key for key, value in d.items()]  # d.items()为字典d的键值对
print(b1)  # ['a', 'g', 'i', 'k']

# 以列表的形式输出字典d的value
b2 = {value for key, value in d.items()}
print(b2)  # {24, 33, 52, 12}

# 颠倒字典d的key:value位置
b3 = {value: key for key, value in d.items()}
print(b3)  # {24: 'a', 52: 'g', 12: 'i', 33: 'k'}

# 将字典d按value的值进行排序    key=lambda x: x[1]  实现
b4 = sorted(d.items(), key=lambda x: x[1])
print(b4)  # [('i', 12), ('a', 24), ('k', 33), ('g', 52)]

'''
sorted(d.items(), key=lambda x: x[1])   中 d.items() 为待排序的对象；
key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序。 
key=lambda  变量：变量[维数] 。维数可以按照自己的需要进行设置。


对函数进行简单说明:
语法：
sorted(d.items(), key=lambda x: x[1])
参数：
d.items() 为待排序的对象
key=lambda 变量：变量[维数]
key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序。
其中x:x[ ]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序，依次类推
'''
# 2、维数以字符串来表示
# 将列表中的age由大到小排序
alist = [{'name1': 'a', 'age': 20}, {'name2': 'b', 'age': 30}, {'name3': 'c', 'age': 25}]
b = sorted(alist, key=lambda x: x['age'], reverse=True)  # reverse 是否逆序
print(b)  # [{'name2': 'b', 'age': 30}, {'name3': 'c', 'age': 25}, {'name1': 'a', 'age': 20}]
