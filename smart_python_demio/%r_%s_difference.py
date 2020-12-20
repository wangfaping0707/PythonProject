# python中%s与%r的区别
x = "a"
y = 'b'
print("%s" % x)
print("%s" % y)
print("%r" % x)
print("%r" % y)
# %s是将变量传到str()函数中，结果是将变量转化适合人阅读的格式
# %r是将变量穿到repr()函数中，结果是将变量转化成适合机器阅读的格式，可以将%r后的变量理解为一个对象

wo = "This is my love 'Big_show'lucky"
print("%s" % wo)
print("%r" % wo)

q = 'This is my love "Big_show"lucky'
print("%s" % wo)
print("%r" % wo)
