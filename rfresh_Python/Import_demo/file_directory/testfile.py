# author ：wang123 
# 创建时间 ：2021/1/31 23:07


def f2(**kwargs):
	return dict(sorted(kwargs.items(), key=lambda item: item[0]))


dict2 = {"name": "wuya", "age": 18, "sex": "male"}

print(dict2.items())

print(f2(**dict2))
