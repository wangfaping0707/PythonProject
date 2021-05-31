class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('出数为零是不合法的。。。。。。。警告。。。。。')
            else:
                raise




cal1 = MuffledCalculator()
# print("返回计算结果：",cal1.calc('10/2'))

# print("关闭了抑制功能，返回计算结果：",cal1.calc('10/0'))

cal1.muffled = True
print("启用了抑制功能，返回计算结果：",cal1.calc('10/0'))