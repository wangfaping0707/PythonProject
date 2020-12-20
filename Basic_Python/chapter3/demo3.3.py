import string

# 1、方法center通过在两边添加填充字符(默认为空格)让字符串居中
print("The Middle by Jimmy Eat World".center(39))

print("The Middle by Jimmy Eat World".center(39, "*"))
print("The Middle by Jimmy Eat World".center(42, "*"))

# 2、方法find在字符串中子串，如果找到，就返回子串的第一个字符的索引，否则返回-1
# in  只能用于检查单个字符是否包含在字符串中
# 字符串方法find返回的并非布尔值，如果find像这样返回0，就意味着它在索引0处找到了指定的子串
print("With a moo-moo here,and a moo-moo there".find("moo"))

title = "Monty Python's Flying Circus"
print(title.find("Monty"))
print(title.find("Python"))
print(title.find("Flying"))
print(title.find("Zirquss"))

# 使用find方法，还可以指定搜索的起点和终点
subject = "$$$ Get rich now!!! $$$"
print(subject.find("$"))

print(subject.find("$$$", 1))  # 只指定了起点
print(subject.find("!!!"))

print(subject.find("$$$", 1, 16))  # 同时指定了起点和终点

# 3、方法join用于合并序列的元素
# seq=[1,2,3,4,5]
seq = ['1', '2', '3', '4', '5']
sep = "+"
print(sep.join(seq))

dirs = '', 'usr', 'bin', 'env'
print("/".join(dirs))

print('C:' + '\\'.join(dirs))
print('C:' + '/'.join(dirs))

# 4、方法lower返回字符串的小写版本
str = "Trondheim Hammer Dance"
print(str.lower())

name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower() in names:
    print('我找到啦：Found it')
else:
    print("我很抱歉，没有找到你要的")

# 5、一个与lower相关的方法是title，它将字符串转换为词首大写，即所有单词的首字母都大写，然而，它确定单词边界
# 的方式有可能导致结果不合理
print("that's all,folks".title())

# 另一种方法是使用模块string中的函数capwords
print(string.capwords("that's all,folks"))

# 6、方法replace将指定子串都替换为另一个字符串，并返回替换后的结果
print('This is a test'.replace('is', 'eez'))

# 7、spilt是一个非常重要的字符串方法，其作用于join相反，用于将字符串拆分为序列
print("1=2=3=4=5=6=7".split("="))

print("/usr/bin/env".split("/"))

# 8、方法strip将字符串开头和末尾的空白(不包括中间的空白)删除，并返回删除后的结果
str = '  The love  '
print(len(str))
print(len(str.strip()))
# strip()方法还可以删除字符串参数中指定要删除那些字符串
str1 = "***SPAM * for * everyone!!! ***"
print(str1.strip(' *!'))  # 这个方法只删除开头或者末尾的指定字符串，因此中间的星号没有被删除
