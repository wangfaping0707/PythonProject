import os

f = open('file.txt')
# print("读出文件file的7个字符:", f.read(7))
# print(f.read(4))
# f.close()

# # 读取文件内容所有内容
# print(f.read())

# # 每次读取文件一行
# for i in range(0,3):
#     print(str(i) + ":" + f.readline(),end="")

print(f.readlines())


