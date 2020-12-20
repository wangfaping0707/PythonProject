# 函数的嵌套,像multiplyByFactor 这样存储其所在作用域的函数称为  闭包 

def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor

    return multiplyByFactor


double = multiplier(17)
print("此时double所代表的类型是：", type(double))
val = double(11)
print(val)


print(multiplier(21)(10))