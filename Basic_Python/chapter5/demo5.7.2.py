from math import *

# scoundrel = {'age': '42', 'first name': 'Robin', 'last name': 'of Locksley'}
# robin = scoundrel
# print('原字典：', scoundrel)
# print('复制后字典：', robin)
# scoundrel = None
#
# # 函数exec将字符串作为代码执行
# exec('print(1+2)')
# exec('print("hello world")')
#
# print("print('Hello,World')")
#
# # exec("sqrt=1")
# # sqrt(4)

scope = {}
scope[sqrt]='1'
exec = ('sqrt=1',scope)
print("平方根值：",sqrt(4))
print(scope)

