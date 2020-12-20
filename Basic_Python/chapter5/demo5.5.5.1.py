# break 要结束(跳出)循环，可使用break
from math import *

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print('root的值：', root)
        print('n的值：', n)
        break;
