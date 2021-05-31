class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)


c1 = CounterList(range(0, 10))
print("打印C1这个对象:", c1)
print(type(c1))
c1.reverse()
print("打印反转后的对象：", c1)
del c1[3:6]
print("打印删除后的c1对象：", c1)
print(c1.counter)
print(c1[0] + c1[1] + c1[2])
print("访问c1属性之后counter的值：", c1.counter)
