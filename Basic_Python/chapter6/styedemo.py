values = (1, 2, 3, 5, 5)

a, b, c, d, e = values

print(a, b, c, d, e)

str = "Hello,"

x1, x2, x3, x4, x5, x6 = str
print(x1, x2, x3, x4, x5, x6)

dict = {"name": "网线", "age": "17"}

print(dict.popitem())


def addStr(str1, str2):
    return str1 + ":" + str2


print(addStr("Hello", "世界"))

print(addStr(str2="世界", str1="Hello"))

labels = 'first', 'middle', 'last'

print(labels)


def adds(a, *b, z):
    print(b)
    return a + z


print(adds(1, 2, 3, 4, 5, 6, 7, 9, z=9))


def call_foo(*args, **kwds):
    print(args)
    print(kwds)


call_foo('a1','b2', 'c1', 1, 2, 3, name="叶玲", age=19, sex="female")
