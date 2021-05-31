from collections.abc import Iterable
"""
在python练习中，遇到关于测试一个对象是否可迭代的过程中，按照教程进行练习，但出现
DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated, and in 3.8 it will stop working
  from collections import Iterable
原因：由于在python3.8中不再支持collections，建议使用collections.abc
 from collections import Iterable   改为   from collections.abc import Iterable
"""

"""
判断一个对象是否可迭代
isinstance(object,classinfo)内置函数可以判断一个对象是否是一个已知的类型，类似 type()。
object -- 实例对象。
classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
在这之前，还需要知道collections模块里的Iterable。通俗点讲，凡是可迭代对象都是这个类的实例对象。下面来验证一下："""

print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({"name": "chichung", "age": 23}, Iterable))
print(isinstance("sex", Iterable))
print(isinstance(123, Iterable))
print(isinstance(True, Iterable))
print(isinstance(1.23, Iterable))

"""
6.可迭代对象怎么可以获取迭代器呢？

看完第4点，有些人就感觉很奇怪，例如：[1,2,3]不就是一个列表，一个对象吗？怎么还能拿出一个迭代器来了？

首先，我们从第5点可以知道，可迭代对象其实都是collections模块里的Iterable类创建出来的实例的。你写一个列表，以为他不是任何类创建的，
只是单纯一个列表？不是的，其实它就是Iterable类创建的实例对象。点进Iterable的类看一下，你会发现新大陆。
class Iterable(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __iter__(self):  # 注意点
        while False:
            yield None
            
原来由Iterable创建的对象，是有一个魔方方法__iter__(self)的。这个方法就是返回一个迭代器的。所以，由Iterable类创建的实例对象，是可以拿出一个迭代器的。
接下来要说的有点绕......
之所以Iterable类创建的对象是可迭代对象，是因为Iterable类有这个方法！不信？我就来编写一个能创建可迭代对象的类。
"""
class BecomeIterable:

    def __iter__(self):
        """返回一个空的迭代器"""
        return None

people = BecomeIterable()
print("people对象是否是可迭代的：",isinstance(people, Iterable))
# 骚不骚？什么都没有，就一个魔法方法，创建的对象就是可迭代对象了。

"""
7.迭代器为什么能用next()函数进行迭代？
我们知道，可以用iter()函数，在可迭代对象中获取迭代器。例如：iterator = iter([1,2,3])
这样一看，迭代器也就是一个对象而已啊，为什么他可以用next()函数，一下子出来一个值，一下子又出来一个值。
其实是这样的，iter()函数能调用可迭代对象的魔方方法__iter__()，从而返回一个迭代器。怎么返回的呢？__iter__()方法是使用collections模块里的Iterator类来创建一个迭代器对象。
接下来看下Iterator的一部分源代码：
class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self
是不是茅塞顿开了？和第6点的解释原理一样。这里就不详细解释了。稍微注意下魔方方法__next__()的最后一句，如果超出迭代方位就抛出StopIteration异常。
还有一点需要注意，迭代器的源代码也有__iter__()魔方方法，所以，Iterator也是一个可迭代对象呀！！！
所以，如果你喜欢在迭代器里面再取出迭代器也是可以的，但是好像有点无聊......目前还不知道有什么应用到......
"""

"""
8.创建一个迭代器类
理论讲完了额...不懂的还是要多看几遍。下面开始应用～
如果我们编写一段代码，想把结果一个一个迭代出来，这时候就需要编写迭代器类了"""
class MyIterator():
    def __init__(self):
        self.list = []
        self.position = 0

    def add_name(self,name):
        self.list.append(name)

    def __iter__(self):
        return self  # 返回一个迭代器

    def __next__(self):
        if self.position < len(self.list):
            item = self.list[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration


people = MyIterator()  # people对象既是一个迭代器，也是一个可迭代对象
people.add_name("张三")
people.add_name("李四")
people.add_name("王五")

# 把people当做一个迭代器来看时
print(next(people))
print(next(people))
print(next(people))

# 把humen当做一个可迭代对象来看时
humen = MyIterator()  # 因为迭代器只能用一次，再用会抛出错误，所以需要再创建
humen.add_name("张三")
humen.add_name("李四")
humen.add_name("王五")
iterator = iter(humen)  # iter()方法获取可迭代对象的迭代器
print(next(iterator))
print(next(iterator))
print(next(iterator))









