
# 包含yield 语句的函数都被称为生成器
# nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
            print('4544')


# 为使用所有的值，可对生成器进行迭代
nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
    print(num)




