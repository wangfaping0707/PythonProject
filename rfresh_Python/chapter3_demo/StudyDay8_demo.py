c = 5


def func1():
    c = 2

    def func2():
        c = 7
        print("func2内部的变量：", c)
    func2()

func1()


def test():
    global a
    if value == 1:
        a += 1
    print(a)


value = a = 1
test()

print(a)

























