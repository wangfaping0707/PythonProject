# 比较运算符：==
print('foo' == 'foo')
print('foo' == 'bar')

# is：相同运算符
# is 运算符检查两个对象是否相同(而不是相等)。变量x和y指向同一个列表，而z指向另一个列表，内存地址不一样，
# 虽然值的内容一样，但并非同一个对象

# 总之，==用于检查两个对象是否相等，而is用来检查两个对象是否相同(是同一个对象)
x = y = [1, 2, 3, 4, 5]
z = [1, 2, 3, 4, 5]
print("x和y是否相等？", x == y)
print("x和z是否相等？", x == z)
print("x is y?", x is y)
print("x is z?", x is z)

print(ord('a'))
print(ord('b'))
print(ord('王'))
print(ord('发'))
print(ord('平'))
print(chr(29579))
print(chr(21457))
print(chr(24179))
# in 成员资格运输符
name = input("请输入你的芳名：")
if 's' in name:
    print("Your name contains the letter 's'!")
else:
    print("Your name does not contains the letter 's'!")
