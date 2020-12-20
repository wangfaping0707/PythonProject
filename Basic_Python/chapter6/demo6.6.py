# 递归 : 一个函数调用自身成为递归

def recursion(depth):
    depth +=1
    print(depth)
    return recursion(depth)


recursion(0)

# 今天在用python写一个递归查询数据库的程序时，报了一个错误：
# RecursionError: maximum recursion depth exceeded in comparison
# 错误的大致意思就是递归超过了最大的深度。


# 查询过相关文档和资料后才发现了问题原因，python的递归深度是有限制的，默认为1000。当递归深度超过1000时，就会报错

# 补充测试
# 由于对最大递归层数产生兴趣，于是我在自己电脑上用以下代码做了测试：
#
# def recursion(depth):
#     depth += 1
#     print(depth)
#     recursion(depth)
#
# recursion(0)