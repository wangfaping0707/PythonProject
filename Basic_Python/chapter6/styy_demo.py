# 方法items返回一个包含所有字典项的列表，其中每个元素为(key,value)的形式，字典项在列表中的排列顺序不确定
dict = {"BJ": "31C", "SH": "29C", "TN": "47C", "AH": "30C"}

print(dict.items())

# 返回值属于一种名为字典视图的特殊类型。字典视图可用于迭代
print(type(dict.items()))

# 遍历字典dict

for key, value in dict.items():
    print(key, ":", value)
print("-------------------------------------------------")
for key1 in dict:
    print(key1, "corresponds", dict[key1])

print(dict.values())

print(dict.keys())

print(dict.items())
