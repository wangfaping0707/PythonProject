class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)


mc = MyClass()
mc.smeth()
MyClass.smeth()
mc.cmeth()
MyClass.cmeth()