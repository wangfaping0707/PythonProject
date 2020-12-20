import time

# 带参数的装饰器(装饰函数)
# 实际是对原有装饰器的一个函数的封装,并返回一个装饰器(一个含有参数的闭包函数),
# 当使用@time_logger(3)调用的时候,Python能发现这一层封装,并将参数传递到装饰器的环境去


def time_logger(flag=0):
    def showtime(func):
        def wrapper(*agrs, **kwargs):
            start_time = time.time()
            func(*agrs, **kwargs)
            end_time = time.time()
            print("执行这个函数需要花费的时间是：", (end_time - start_time))

            if flag:
                print("将此操作保留到日志。。。。。。")

        return wrapper

    return showtime


@time_logger(3)   # 得到闭包函数showtime,add = showtime(add)
def add(a, b):
    print("add函数的执行结果：", (a + b))
    time.sleep(3)


add(9, 9)
