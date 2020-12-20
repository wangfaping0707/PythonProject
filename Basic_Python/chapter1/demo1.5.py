print('"Hello,world!",she said\\df')

print('Let\'s go!')

print('Let\'s say "hello,world!"')

# 拼接字符串
x = "hello,"
y = "world"
print(x + y)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# \n 是换行符
# print("Hello,\nWorld")
# 使用str能以合理的方式将值转换为用户能够看懂的字符串。例如：尽可能将特殊字符编码转换为相应的字符串
# 使用repr时，通常会获得值的合法表达式
print("使用str进行字符串打印：%s" % (str("Hello,\nWorld")))
print("使用repr进行字符串打印：%s" % (repr("Hello,\nWorld")))

# 演示跨越多行的字符串
print("Hello,\
 World")

path1 = 'C:\\nowhere'
print(path1)
path2 = 'D:\\ProgramFiles\\fnord\\foo\\bar\\frozz\\bozz'
print(path2)
# 原始字符串不以特殊方式处理反斜杠，原始字符串用前缀r表示。看起来可在字符串中包含任何字符
path3 = 'E:\ProgramFiles\fnord\foo\bar\frozz\bozz'
print(path3)
print(r'E:\ProgramFiles\fnord\foo\bar\frozz\bozz')

print('C:\\Program Files\\foo\\bar\\')
print(r'C:\Program Files\foo\bar''\\')
print("This is a cat: \N{Cat}")
print("This is a Dog: \N{Dog}")
print("This is a Pig: \N{Pig}")
print(len(path3.encode("UTF-8")))
print(len(path3.encode("UTF-32")))
