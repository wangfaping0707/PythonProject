

list = ['打桩', 'dhd', 3, 4, '漂亮']
# next(list)

# __next__()的作用是返回遍历过程中的下一个元素，如果没有下一个元素则主动抛出StopIteration异常。
# 而next()就是Python提供的一个用于调用__next__()方法的内置方法。
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))