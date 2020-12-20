"""
枚举的定义
首先，定义枚举要导入enum模块。
枚举定义用class关键字，继承Enum类
定义枚举时，成员名称不允许重复
默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名　
如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
如果枚举有值重复的成员，循环遍历枚举时只获取值重复成员的第一个成员
如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__
如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
from enum import Enum, unique
@unique
class Color(Enum):
    red = 1
    red_alias = 1
"""
import enum


class VIP(enum.Enum):
    YELLOW = 1
    BLACK = 2
    GREEN = 3
    PINK = 4
    RED= 1


# VIP.BLACK = 101


print(VIP.BLACK)
print("通过成员的名称来获取成员：", VIP['YELLOW'])
print("通过成员值来获取成员：", VIP(1))
print("通过成员，来获取它的名称和值:", VIP.BLACK.name, "--->", VIP.BLACK.value)  # 获取标签对应的值
print(VIP.BLACK.name)    # 获取标签对应的名字
print("鉴别", VIP.YELLOW)
print("鉴别", VIP.RED)

# 枚举支持迭代器，可以遍历枚举成员   使用print(color.value) 可以打印出所有成员的值. 1 2 3 4 5 6 7
print("--------------------------枚举迭代1---------------------")
for vip in VIP:
    print(vip, ":", vip.value)

print("--------------------------枚举迭代2----------------------")
for vip in VIP.__members__:
    print(vip)

print("--------------------------枚举迭代3----------------------")
for vip in VIP.__members__.items():
    print(vip)


# 枚举成员可进行同一性比较

result = VIP.YELLOW is VIP.YELLOW
result1 = VIP.YELLOW is VIP.BLACK
print("身份校验：", result, result1)

#  枚举成员可进等值比较
result2 = VIP.YELLOW == VIP.RED
result3 = VIP.YELLOW ==VIP.BLACK
print("枚举成员值比较大小：", result2, result3)

# 枚举成员不能进行大小比较

# result4 = VIP.BLACK > VIP.YELLOW
# print(result4)
