print(list("hello"))
print(type(list("hello")))

h = ["w", "u", "m", "e", "i"]
str = ''.join(h)
print("我的内容：%s" % str[2])
print(type(str))
print("删除之后字符str的内容为：%s" % str)

m = [1, 1, 1, 1, 1]
m[2] = 10
# m [110]=11
print(m)
# 删除元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
print("删除之前列表的names的长度为：%d" % len(names))
del names[2]
print(names)
print("删除之后列表的names的长度为：%d" % len(names))

# 给切片赋值
name = list("Perl")
print(name)
name[2:] = list('wang')
print(name)

n = ['w', 'a', 'n', 'w']
print(type(n))
n[1:3]=list('faPING')
print(n)

