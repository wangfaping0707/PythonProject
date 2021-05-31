"""
Python JSON :本章节我们将为大家介绍如何使用 Python 语言来编码和解码 JSON 对象。
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写
JSON 函数 : 使用 JSON 函数需要导入 json 库：import json。
json.dumps : 将 Python 对象编码成 JSON 字符串                       俗称序列化
json.loads ：将已编码的 JSON 字符串解码为 Python 对象                俗称反序列化
"""
import json

# 以下实例将数组编码为 JSON 格式数据
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
print(type(data))
data2 = json.dumps(data)
print(data2)
print(type(data2))

"""
json.loads
json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
以下实例展示了Python 如何解码 JSON 对象：
"""
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

print(type(jsonData))

text = json.loads(jsonData)
print(text)
print(type(text))

















