# 方法fromkeys 创建一个新字典，其中包含指定的键，且每个键对应的值都是None
dict1 = {}.fromkeys("name", "age")
print(dict)
# 这个例首先创建一个空字典，在对其调用方法fromkeys来创建另一个字典
dict2 = {}.fromkeys(('name', 'age'))
print(dict2)

# dict是所有字典所属的类型
d = dict.fromkeys(['name', 'age'])
print(d)

d1 = dict.fromkeys(['a', 'b', 'c'], ('10', '11'))
print(d1)

d3 = {}
# print(d3["a"])
print(d3.get('name'))
# 使用get来访问不存在的键时，没有引发异常，而是返回None。你可指定”默认值“，这样将返回你指定的值而不是None
print(d3.get('name','N/A'))

# 如果字典包含指定的键，get的作用将于普通字典查找相同
d3["name"]="Eric"
print(d3.get("name",'N/A'))