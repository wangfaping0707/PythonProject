class FooBar:
    def __init__(self,value = 90):
        self.somevar = value


f = FooBar()
print("打印对象f的变量值:", f.somevar)
f1 = FooBar("This is a constructor argument")
print("打印对象f1的变量值:", f1.somevar)

