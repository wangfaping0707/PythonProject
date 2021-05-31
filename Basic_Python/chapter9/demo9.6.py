"""
python中的迭代器详解:
1.迭代是什么？
我们知道可以对list,tuple,dict,str等数据类型使用for...in的循环语法，从其中依次取出数据，这个过程叫做遍历，也叫迭代。迭代是访问集合元素的一种常用的方式。

2.可迭代对象是什么？
简单来说，可以用for...in循环语句，从其中依次取出数据的对象，就是可迭代对象。例如，列表、元组、字典、字符串都是可迭代对象。整数、浮点数、布尔值都是不可迭代的。

3.迭代器是什么？

在可迭代对象进行迭代的时候，即用for...in...循环语法依次取出数据时，过程是怎样的呢？

我们发现，每迭代一次（即在for...in...中每循环一次）都会返回对象中的下一条数据，一直向后读取数据直到迭代了所有数据后结束。
那么，在这个过程中就应该有一个“人”去记录每次访问到了第几条数据，以便每次迭代都可以返回下一条数据。
我们把这个能帮助我们进行数据迭代的“人”称为迭代器(Iterator)。举个栗子，
老师安排一个班的同学每节课上课前进行演讲，按学号顺序进行，A同学这节课演讲，
老师就会记住这节课是A同学演讲，那么下节课就是B同学进行演讲...依次类推，
在这个例子里，老师就是一个迭代器。

4.怎样获取可迭代对象的迭代器？
我们可以通过iter()内置函数取得可迭代对象的迭代器。
"""
# list是个可迭代的对象
list = [1, 2, 3, 4, 5]
# 通过iter()方法取得list的迭代器
# 对一个对象调用iter()可以得到他的迭代器
Iterator = iter(list)
print(Iterator)

"""
迭代器是获取到了，那么应该怎样用呢？
next()函数是通过迭代器获取下一个位置的值。
注意: 当我们已经迭代完最后一个数据之后，再次调用next()函数会抛出StopIteration的异常，来告诉我们所有数据都已迭代完成，不用再执行next()函数了。
"""
list1 = [1,2, 3, 4]
Iterator1 = iter(list1)
print(next(Iterator1))
print(next(Iterator1))
print(next(Iterator1))
print(next(Iterator1))
print(next(Iterator1))

# try:
#     Iterator1 = iter(list1)
#     # for x in Iterator1:
#     #     print("输出列表的元素：", x)
#     #     # print(type(Iterator1))
#     print(next(Iterator1))
#     print(next(Iterator1))
#     print(next(Iterator1))
#     print(next(Iterator1))
#     print(next(Iterator1))
# except Exception as e:
#     print(e)
#     print(type(e))

