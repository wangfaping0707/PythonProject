# 计算n的阶乘
# 方式一
def factorial(n):
    result = n
    for i in range(1, n):
        result = result * i
    return result


print("方式一求值n阶乘：", factorial(10))


# 阶乘的数学定义，可表述如下：
# 1的阶乘为1
# 对于大于1的数字n,其阶乘为n-1的阶乘乘以个n

def factoriall(n):
    if n == 1:
        return 1
    else:
        return n * factoriall(n - 1)


# 函数调用factoriall(n)和factoriall(n-1)是不同的实体

print("方式二求值n阶乘：", factoriall(10))


# 计算幂

def power(x, n):
    result = 1
    for i in range(n):
        result = result * x
    return result


print("方式一求值x的幂：", power(2, 5))


def power1(x, n):
    if n == 0:
        return 1
    else:
        return x * power1(x, n - 1)


print("方式二求值x的幂：", power1(2, 5))
