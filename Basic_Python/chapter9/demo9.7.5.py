"""
1.生成器的创建与元素迭代遍历
1.1创建生成器方法1：只要把一个列表生成式的 [ ] 改成 ( )
  生成器(generator)其实是一类特殊的迭代器。前面博客我们每次迭代获取数据（通过next()方法）时按照特定的规律进行生成。
  但是我们在实现一个迭代器时，关于当前迭代到的状态需要我们自己记录，进而才能根据当前状态生成下一个数据。为了达到记录当前状态，
  并配合next()函数进行迭代使用，python就搞了个生成器。所以说生成器(generator)其实是一类特殊的迭代器。

#1.创建生成器
ls = [x*2 for x in range(10)]
generator1 =(x*2 for x in range(10)) #这是一个生成器generator
print(ls)
print(generator1) #注意，打印生成器，不会像列表一样打印他的值，而是地址。
'''
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
<generator object <genexpr> at 0x00000239FE00A620>
'''
"""
ls = (x * 2 for x in range(10))
print("ls的类型是：", type(ls))
print(ls)

"""
遍历生成器对象中的内容：
1.方法1.使用for循环遍历
for i in generator1:
    print(i)

#方法2：命令行使用next()函数：调用next(G) ，就计算出 G 的下一个元素的值，直到计算到最后一个元素
没有更多的元素时，抛出 StopIteration 的异常。
>>> generator1 =(x*2 for x in range(5))
>>> next(generator1)
0
>>> next(generator1)
2
>>> next(generator1)
4
>>> next(generator1)
6
>>> next(generator1)
8
>>> next(generator1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""
for i in ls:
    print(i)
"""
2.方法2.python脚本使用next()方法，实际开发中是通过for循环来实现遍历，这种next()方法太麻烦。
g1 =(x*2 for x in range(5))
while True:
    try:
        x = next(g1)
        print(x)
    except StopIteration as  e :
        print("values=%s"%e.value)
        break #注意这里要加break,否则会死循环。
'''结果如下：
0
2
4
6
8
values=None
3.方法3：使用对象自带的__next__()方法，效果等同于next(g1)函数
>>> g1 =(x*2 for x in range(5))
>>> g1.__next__()
0
>>> g1.__next__()
2
>>> g1.__next__()
4
>>> g1.__next__()
6
>>> g1.__next__()
8
>>> g1.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""
print("-----------------------------------------分割线-------------------------------------------")

"""
#著名的斐波拉契数列（Fibonacci）:除第一个和第二个数外，任意一个数都可由前两个数相加得到
#1.举例：1, 1, 2, 3, 5, 8, 13, 21, 34, ...使用函数实现打印数列的任意前n项。
def fib(times): #times表示打印斐波拉契数列的前times位。
    n = 0
    a,b = 0,1
    while n<times:
    
        print(b)
        a,b = b,a+b
        n+=1
    return 'done'
 
fib(10)  #前10位：1 1 2 3 5 8 13 21 34 55

#2.将print(b)换成yield b,则函数会变成generator生成器。
#yield b功能是：每次执行到有yield的时候，会返回yield后面b的值给函数并且函数会暂停，直到下次调用或迭代终止；
def fib(times): #times表示打印斐波拉契数列的前times位。
    n = 0
    a,b = 0,1
    while n<times:
        yield b  
        a,b = b,a+b
        n+=1
    return 'done'
 
print(fib(10))  #<generator object fib at 0x000001659333A3B8>

3.对生成器进行迭代遍历元素
方法1：使用for循环
for x in fib(6):
    print(x)
''''结果如下，发现如何生成器是函数的话，使用for遍历，无法获取函数的返回值。
1
1
2
3
5
8
'''
方法2:使用next()函数来遍历迭代，可以获取生成器函数的返回值。同理也可以使用自带的__next__()函数，效果一样
f = fib(6)
while True:
    try:  #因为不停调用next会报异常，所以要捕捉处理异常。
        x = next(f)  #注意这里不能直接写next(fib(6)),否则每次都是重复调用1
        print(x)
    except StopIteration as e:
        print("生成器返回值:%s"%e.value)
        break
'''结果如下：
1
1
2
3
5
8
生成器返回值:done

"""


def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        print(b)
        a, b = b, a + b
        n += 1
    return "done"


fib(10)
