class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height


r = Rectangle()
print("对象r所具有的属性：", r.__dict__)
r.width = 10
r.height = 5
print("r重新设置的属性值：", r.get_size())
# 再次通过方法来设置对象r的属性值
r.set_size((105, 209))
print("通过方法重新设置r的属性值：", r.get_size())

f = 1, 2, 3
print("f的类型：", type(f))


