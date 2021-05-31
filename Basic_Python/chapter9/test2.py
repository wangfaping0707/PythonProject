from collections.abc import Iterator,Iterable


class A():
    def __iter__(self):
        print("A类的__iter__方法被调用")
        return B()


class B():
    def __iter__(self):
        print("B类的__iter__方法被调用")
        return self

    def __next__(self):
        print("德玛西亚")



a = A()
print("a是可迭代的对象吗？",isinstance(a,Iterable))
print("a是迭代器吗？",isinstance(a,Iterator))
print("-----------------------风隔线-------------------------------")
# 方法一
a1 = iter(a)
print('a1是可迭代的对象吗？：', isinstance(a1, Iterable))
print('对A类对象调用iter()方法后，a1是迭代器吗：', isinstance(a1, Iterator))
print("-----------------------风隔线-------------------------------")
# 方法二
a2 = a.__iter__()
print('a2是可迭代的对象吗？：', isinstance(a2, Iterable))
print('调用a的方法__iter()___，a2是迭代器吗：', isinstance(a2, Iterator))

print("-----------------------风隔线-------------------------------")
b = B()
print('b是可迭代的对象吗？：', isinstance(b, Iterable))
print('b是迭代器吗？', isinstance(b, Iterator))














