# 闭包 = 函数 + 环境变量
def curve_pre():
    a = 0

    def curve(x):
        return a * x * x
    return curve


a = 10
f = curve_pre()
print("f的类型是：", type(f))
result = f(2)
print("调用内层函数：", result)
