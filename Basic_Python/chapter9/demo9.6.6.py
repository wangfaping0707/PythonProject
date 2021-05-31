"""
迭代器就是有一个next()方法的对象，而不是通过索引来计数。
如何创建迭代器?

1、调用iter()函数
对一个对象调用iter()可以得到他的迭代器
"""


def iter_test():
    it = iter('happy')
    try:
        while True:
            print(next(it))
    except StopIteration:
        print('你过界了，少年？')
    print('----------------------风格线--------------------------')
    s = {'one': 1, 'two': 2, 'three': 3}
    print(s)
    m = iter(s)
    try:
        while True:
            print(next(m))
    except StopIteration:
        print('遍历已完成')


if __name__ == '__main__':
    iter_test()
