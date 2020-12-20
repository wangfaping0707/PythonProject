# 关键字可变参数
def squsum(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)


squsum(1, 2, 3, 4, 5, 6)


# 函数的可变关键字参数
def city_temp(**param):
    for k, v in param.items():
        print(k, ":", v)
    print(param)
    print(type(param))


city_temp(bj="34c", cd="27c", sh="35c", hz="28c")

dict = {"name:": "小雨", "age": 21, "gender": "female", "food": "大饼"}

print(dict.keys())
print(dict.values())
#
# items()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回
print(dict.items())

for key, value in dict.items(): # 用到序列解包方法
    print(key, ":", value)

print("-----------------------------------------")
for c in dict:
    print(dict[c])

# 序列解包
a, b, c = (1, 2, 3)
print(a, b, c)
