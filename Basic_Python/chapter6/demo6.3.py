# 自定义函数
# 函数执行特定的操作，并返回一个值(有的函数没有返回值)，你可以调用它。
# 一般而言，判断某个对象是否可调用，可使用内置函数callable
import math

x = 1
y = math.sqrt

print("x是否可调用?", callable(x))
print("y是否可调用?", callable(y))


# 函数是结构化编程的核心，那么如何定义函数呢？使用def (表示定义函数) 语句

def hello(name):
    return "Hello," + name + '!'


print(hello("wumeifang"))
print(hello("Gumby"))


def fibs(num):
    result = [0, 1]
    for i in range(num):
        result.append(result[-2] + result[-1])
    return result


print("斐波那契数组成的列表：", fibs(-2))
print("斐波那契数组成的列表：", fibs(10))
print("斐波那契数组成的列表：", fibs(15))


# 给函数编写文档
# _doc_是函数的一个属性，属性名中的双下划线表示这是一个特殊的属性
def square(x):
    "Calculates the square of the number x."
    "我是函数的注释，请知悉，"
    return x * x


print(square.__doc__)


def test():
    print("我就是一个打印大神")
    return
    print("我就看看我是否被执行了")


x = test()
print(test())

print("x到底是什么类型？", type(x))


def add(x, y):
    result = x + y
    return result


print(add(4, 9))

# print(add(9,"wl"))
