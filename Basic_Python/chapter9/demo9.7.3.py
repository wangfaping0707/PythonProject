def test():
    i = 0
    while i < 5:
        temp = yield i
        print("第%d次打印" % (i), temp)
        i += 1


a = test()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())