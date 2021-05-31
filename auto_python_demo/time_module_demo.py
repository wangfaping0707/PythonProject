# 练习使用python中的time模块

import time as t

# 时间戳类型
# 从初始时间到指定时间的秒数。
# 例如，time.time()得到的float类型的秒数
# 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。
print("当前时间戳为：", t.time())

# 获取当前时间：从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
localtime = t.localtime(t.time())
print("本地时间为：", localtime)

# 获取格式化的时间：你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()

format_time = t.asctime(t.localtime())
print("格式化的时间为：", format_time)

# 格式化日期:我们可以使用 time 模块的 strftime 方法来格式化日期:

FORMAT_TIME = t.strftime("%Y-%m-%d %H:%M:%S", t.localtime())
print("打印格式化后的时间", FORMAT_TIME)
