# author ：wang123 
# 创建时间 ：2021/1/25 23:48


def f1(*args, **kwargs):
	print(args, kwargs)
	print(type(args))
	print(type(kwargs))


f1(1, 2, 3, 4, 5, 6)
f1(x=1, y=3, c=7)
f1("n", "b", "c", name="wuya", age="23", sex="male")
print("----------------------------------------------------------------")
dict1 = {"name": "wuya", "age": 19, "sex": "male"}
print(list(dict1.items()))

