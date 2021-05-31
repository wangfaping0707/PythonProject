from collections.abc import Iterator,Iterable
import sys
#     2、也可以使用 next() 函数：
list1 = [7,8,9,0]
it1 = iter(list1) # 创建迭代器对象
while True:
    try:
        print(next(it1))
    except StopIteration as  e:
        print("已经迭代完毕，退出")
        sys.exit()