
# times表示打印斐波拉契数列的前times位。


def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


print(fib(10))

print("****************************************************************")

for x in fib(10):
    print("迭代x的值：",x)


print('-----------------分割线---------------------')


f = fib(17)

while True:
    try:
        # y = next(f)  方法1
        # 方法2
        y = f.__next__()
        print("迭代y的值：",y)
    except StopIteration as e:
        print(e.value)
        break

"""
生成器使用总结：

1.生成器的好处是可以一边循环一边进行计算，不用一下子就生成一个很大的集合，占用内存空间。生成器的使用节省内存空间。

2.生成器保存的是算法，而列表保存的计算后的内容，所以同样内容的话生成器占用内存小，而列表占用内存大。每次调用 next(G) ，
  就计算出 G 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration 的异常。
  
3.使用for 循环来遍历生成器内容，因为生成器也是可迭代对象。通过 for 循环来迭代它，不需要关心 StopIteration 异常。
  但是用for循环调用generator时，得不到generator的return语句的返回值。如果想要拿到返回值，必须用next()方法，且捕获StopIteration错误，返回值包含在StopIteration的value中。
  
4.在 Python 中，使用了 yield 的函数都可被称为生成器（generator）。生成器是一个返回迭代器的函数，只能用于迭代操作。更简单点理解生成器就是一个迭代器。

5.一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
  直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
  保存当前所有的运行信息，并返回一个迭代值，下次执行next() 方法时从 yield 的下一个语句继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。生成器不仅“记住”了它数据状态；生成器还“记住”了它在流控制构造中的位置。
 
版权声明：本文为CSDN博主「涤生手记」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_26442553/article/details/82418257


"""