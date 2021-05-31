# 创建自定义类

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello,world! I'm {}".format(self.name))

    def hellp(self):
        print("你好，这世界，我来了")


foo = Person()
bar = Person()

foo.set_name('Luke Skywalker')
bar.set_name("Anakin Skywalker")

foo.greet()
bar.greet()
foo.hellp()

foo.name = 'wry43'
print(foo.name)
