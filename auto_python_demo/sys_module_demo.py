import sys

print(sys.argv)
print("结果类型是：", type(sys.argv))
print("命令行参数如下：")
for i in sys.argv:
    print(i)


# 打印出python的版本号
print("当前python的版本号：", sys.version)
print("当前操作平台：", sys.platform)

print(sys.path)
