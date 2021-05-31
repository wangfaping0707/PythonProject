import json

# dumps可以格式化所有的基本数据类型为字符串
data = []
print("data的数据类型", type(data), data)
data1 = json.dumps(data)
print("data1的数据类型", type(data1), data1)
print("----------------------分隔线-----------------------")
data2 = 345
print("data2的数据类型", type(data2), data2)
data22 = json.dumps(data2)
print("data22的数据类型", type(data22), data22)

print("----------------------分隔线-----------------------")
dict11 = {"name": "Tom", "age": 18}  # 字典
data4 = json.dumps(dict11)
print(data4, type(data4))

dict = {'name': '赫卡里姆', 'age': 799, 'favorite': ['music', 'swim', 'reading'], 'cook': '美食', '运动': '打球', '学历': '博士后'}
print("dict的数据类型：", type(dict))

with open("testJson.txt", 'a+', encoding='utf-8') as  f:
    json.dump(dict, f, ensure_ascii=False)
