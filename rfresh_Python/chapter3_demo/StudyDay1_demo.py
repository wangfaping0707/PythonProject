
# 以 # 开头的注释可以注释一行文本，Python 另外提供了注释多行文
# 本的功能。多行注释用三个单引号 ‘’’ 或者三个双引号 “”" 将注释括起来，例如:
# 使用3个单引号注释多行文本


'''
# 首先定义变量 x
# 让后将变量 x 修改为 456
x = 123
x = 456
'''

"""
# 首先定义变量 x
# 让后将变量 x 修改为 456
x = 123
x = 456
"""

# 输入与输出，Python 提供了 input 语句用于读取键盘输入，input 语句读取用户输入的一行文本。

line = input()
print(line)

# 在第 1 行，使用 input 语句读取用户输入的一行文本，将该文本保存到变量 line 中。
# 在第 2 行，用户输入一行文本 ‘hello world’。
# 在第 3 行，查看变量 line。
# 在第 4 行，显示结果为文本 ‘hello world’

# 可以在 input 语句中加入参数，该参数作为用户输入的提示符，例如：

number = input('Please input a number: ')
print(number)

# 在第 1 行，使用 input 语句读取用户输入的一行文本，将该文本保存到变量 number 中。input 语句带有一个参数 'Please input a number: '。
# 在第 2 行，input 语句首先输出 input 语句的参数 'Please input a number: '，这样用户就根据该提示输入数
# 字，然后 input 语句再读取用户输入的一行文本 123。


# 使用 print 语句输出多项内容: 在输入中，每项内容使用逗号分开  在输出中，每项内容使用空格分开

print(123, 'hello world', 1 + 1, "1+1")

