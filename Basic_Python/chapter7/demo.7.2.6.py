class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

# SPAMFilter类是Filter类的子类
class SPAMFilter(Filter):
    # 重写超类Filter的方法init
    def init(self):
        self.blocked = ['SPAM']


f = Filter()
print(f.init())
print(f.filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))

s = SPAMFilter()
print(s.init())
print(s.filter(['SPAM',123,345,'SPAM',9028,'SPAM']))


# 要确定一个类是否是另一类的子类，可使用内置方法issubclass
print(issubclass(SPAMFilter,Filter))
print(issubclass(Filter,SPAMFilter))

# 如果你有一个类，并想知道它的基类，可访问其特殊的属性__bases__
print(SPAMFilter.__bases__)
print(Filter.__bases__)

# 要确定对象是否是特定类的实例，可使用isstance
s = SPAMFilter()
print(isinstance(s,SPAMFilter))




print(isinstance(s,Filter))

# 如果要获悉对象属于那个类，可使用属性__class__
print(s.__class__)

print(type(s))








