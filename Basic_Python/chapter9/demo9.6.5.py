"""
StopIteration:
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
在 20 次迭代后停止执行：
"""
from collections.abc import Iterator, Iterable


class MyNum:
    def __iter__(self):
        self.start_first_num = 1
        return self

    def __next__(self):
        if self.start_first_num <= 20:
            x = self.start_first_num
            self.start_first_num += 1
            return x
        else:
            raise StopIteration


mn = MyNum()
print("判断mn是否是一个可迭代的对象？", isinstance(mn, Iterable))
print("mn本身是否是一个迭代器？", isinstance(mn, Iterator))
my_iter = iter(mn)
for x in my_iter:
    print(x, end=" ")
