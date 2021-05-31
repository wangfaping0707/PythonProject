"""
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
Iterable  可迭代的 ————》形容词
Iterator  迭代器————》名词
"""
from collections.abc import Iterable,Iterator
import sys
list = [1,2,3,4]
# 判断list是否是一个可迭代的对象
print("list是否可迭代：",isinstance(list,Iterable))
print("list是否是一个迭代器：：",isinstance(list,Iterator))

# 通过iter()方法取得list的迭代器
# 对一个对象调用iter()可以得到他的迭代器
it = iter(list)  # 创建list的 迭代器对象    迭代器就是用于记录迭代中每次遍历的位置
print("看一下迭代器究竟是什么？",)
print("迭代器类型是什么？",type(it))
print(next(it))  # 输出迭代器的下一个元素

#     1、迭代器对象可以使用常规for语句进行遍历：
for x in it:
    print(x,end="/")

















