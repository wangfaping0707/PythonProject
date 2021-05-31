from collections.abc import Iterable, Iterator


class A():
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        print("A类的__iter__()方法被调用----------")
        return B(self.lst)


class B():
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        print("B.__iter__()方法被调用")
        return self

    def __next__(self):
        try:
            print('B.__next__()方法被调用')
            value = self.lst[self.index]
            self.index += 1
            return value
        except IndexError as  e:
            print("索引越界了啊啊啊啊啊。。。。。")
            print(e.args)
            raise StopIteration()


a = A([6, 5, 43, 343])
a1 = iter(a)
print(next(a1))
print("---------------------------------------")
print(next(a1))
print("---------------------------------------")
print(next(a1))
print("---------------------------------------")
print(next(a1))
# print("---------------------------------------")
# print(next(a1))

"""
A类实例化出来的实例a只是可迭代对象，不是迭代器，调用iter()方法后，返回了一个B类的实例a1，每次对a1调用next()方法，都用调用B类的__next__()方法。
接下来，我们用for循环遍历一下A类实例："""
print("*******************************************************")
for i in A([1,2,3,4]):
    print('for循环中取出值:',i)



























