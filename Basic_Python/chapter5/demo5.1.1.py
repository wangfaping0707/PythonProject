# print可用于打印一个表达式，这个表达式要么是字符串，要么将自动转换为字符串，但实际上，你可以同时打印多个表达式
# 条件是用逗号分隔它们
print("age：", 31)
list = ['我', '1', 'love']
print("这是一个列表：", list)

name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello,'
print(greeting + salutation + name)
print(greeting, salutation, name)

print(greeting, ',', salutation, name)
print("-----------------------------")
print(greeting+',',salutation,name)
print('I', 'wish', 'to', 'register', 'a', 'complaint', sep='_')

print('Hello' + ",", end='')
print('world!')



