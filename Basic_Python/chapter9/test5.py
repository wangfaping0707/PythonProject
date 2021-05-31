from collections.abc import Iterator,Iterable


def gen():
    print("第1次执行")
    yield 1
    print("第2次执行")
    yield 2
    print("第3次执行")
    yield 3


g = gen()
print('g是可迭代对象吗？',isinstance(g,Iterable))
print("g是迭代器吗？",isinstance(g,Iterator))
print("******************************************************************************")
print(next(g))
print(next(g))
print(next(g))
























