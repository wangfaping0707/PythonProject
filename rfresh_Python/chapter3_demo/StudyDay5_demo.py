
a = 2.6750
print(round(a, 2))


def add(x, y):
    print("输入的参数x:", x)
    print("输入的参数y:", y)
    return x + y


print("www", "runoob", "com", sep=".")


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2


# 函数的多个返回值会组装成元组
# damages = damage(2, 7)
# print(type(damages))

# 可以用序列解包的方式来接受函数的多个返回值

skill1_damage, skill2_damage = damage(3, 7)
print(skill1_damage, skill2_damage)
