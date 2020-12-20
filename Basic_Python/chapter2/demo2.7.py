# 列表方法：方法是与对象(列表、数、字符串等)联系紧密的函数。通常可采用下面这样调用方法：
# object.method(arguments)
# 1、append方法：用于将一个对象添加到列表末尾
number = [1, 2, 3]
number.append(4)
print(number)
# 2、方法clear清楚列表中的内容
number.clear()
print(number)
# 3、方法copy用于复制列表，前面说过，常规复制只是将另一个名称关联到列表
a = [9, 7, 0, 4]
b = a.copy()
print(b)
b[2] = 18
print(b)
print("-------------------------------")
print(a)

# 4、方法count计算指定的元素在列表中出现了多少次
strOfList = ['to', 'be', 'or', 'not', 'to', 'be', 'to']
print(strOfList.count('to'))

# 5、方法extend让你能够同时将多个值附加到列表末尾，为此可将这些值组成序列作为参数提供给方法extend。换而言之，你可
# 使用一个列表来扩展另一个列表
a = ['1', '2', '3']
b = ['w', 'a', 'n', 'g']
# a.append(b)
a.extend(b)
print(a)

# 6、方法index在列表中查找指定值第一次出现的索引
knights = ['we', 'are', 'the', 'who', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))

# 7、方法insert用于将一个对象插入列表
num = [1, 2, 3, 4, 5, 6, 7]
num.insert(3, '你好')
print(num)

# 8、方法pop从列表中删除一个元素(默认为最后一个元素)，并返回这一元素
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s1 = x.pop()
print(s1)
print(x)
s2 = x.pop(3)
print(s2)
print(x)

# 9、方法remove用于删除第一个为指定值的元素
# remove是就地修改且不返回值的方法之一。不同于pop的是，他修改列表，但不返回任何值
x = ["to", "be", "or", "not", "to", "be", "ok"]
x.remove("be")
print(x)

# 10、方法reverse按相反的顺序排列列表中的元素
y = [1, 2, 3, 4, 5]
y.reverse()
print(y)

# 11、方法sort用于对列表就地排序
z = [4, 22, 0, 1, 14, 17, 6, 99, 10, 45, 24]
z.sort()
print(z)
z1 = ['q', 'bc', 'wa', 'd']
z1.sort()
print(z1)

str1 = 'dfkanbyc'
x1 = sorted(str1)
print(x1)

# 高级排序
x2 = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x2.sort(key = len)
print(x2)

x3=[4,6,2,1,7,9]
x3.sort(reverse=False)
print(x3)