# 属性 函数和方法
class example:
    name = 'lover'

    def method(self):
        print("打印方式一", 'I have a {}'.format(self.name))
        print("打印方式二", 'I have a %s' % self.name)

    def function(self):
        print("I don't ..........")

# 在python中，函数名加（），表示返回的是一个函数的计算结果，不加括号表示的是对函数的调用，是函数的一个地址。
instance = example()
print(instance)
instance.method()
instance.function()

print(instance.method)





