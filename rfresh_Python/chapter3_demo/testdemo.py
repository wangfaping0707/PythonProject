import re
"""
e.sub()的第二个参数传入一个函数时，它的流程是：当匹配到第一个 C# 时，
会把匹配的结果传入这个函数中，也就是 C# 会作为 convert函数的value传入，convert 函数的返回结果回用于替换原字符串中的 C#
因此如上例子中，convert函数并未返回，所以C# 全部消失
但是要注意，此处传入的 C# ，并不是简单的以字符串的方式传入，而是作为一个对象
"""


def convert(value):
    # print(value)
    matched = value.group()
    print("打印match对象：", matched)
    return '!!' + matched + '!!'


k = 'PythonC#JavaPHPC#C#C#'
r = re.sub('C#', convert, k)
print(r)


"""
把函数作为参数传递
找出字符串中的所有数字，大于等于 6 时替换为 9，小于 6 替换为 0：
"""

a = 'A8C3467290'


def convert(value):
    matched = value.group()
    if int(matched) >= 6:  # 注意字符串转为 int
        return '9'  # 返回值必须是string
    else:
        return '0'


r = re.sub('\d', convert, a)  # 每找到一个数字，就调用convert一次
print(r)  # A9C0099090

# 练习：传入的字符串字母和数字夹杂，数字分为一位和两位，
# 要求剔除所有一位的数字，剩下的大于等于50 替换为99，小于50 替换为0：

b = "A83C12D1D8E67"


def convert1(value):
    matcher = value.group()
    if int(matcher) >= 50:
        return "99"
    else:
        return "0"


regex = "\\d{1,2}"  # 匹配一到两位数字
rs = re.sub(regex, convert1, b)
print(rs)
































