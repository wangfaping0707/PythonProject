# 迭代字典
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, ':', d[key])
    # print(d.keys())
    # print(d.values())
    print(d.items())

dict = {'name': 'wumeifang', 'age': '30', 'sex': 'female'}
for key, value in dict.items():
    print(key, ":", value)
