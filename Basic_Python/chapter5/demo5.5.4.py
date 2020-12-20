# 并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# 如果要打印名字和对应的年龄，可以如下操作
for i in range(0, len(names)):
    print(names[i], 'is', ages[i], 'years old')

# 并行迭代根据：内置函数zip，它将两个序列缝合起来，并返回一个由元组组成的序列
print(zip(names, ages))
print(type(zip(names, ages)))

print(list(zip(names, ages)))
print(dict(zip(names, ages)))

for name, age in zip(names, ages):
    print(name, 'is', age, "years old")
