def add(x, y):
    return x + y


f = lambda x, y: x + y

print(add(3, 4))
print(f(3, 4))

# python的三元运算符
a = 5
b = 3

r = a if a > b else b
print(r)
