"""
Python JSON
本章节我们将为大家介绍如何使用 Python 语言来编码和解码 JSON 对象。
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
JSON 函数:  使用 JSON 函数需要导入 json 库：import json。
函数：
json.loads   ----》	将已编码的 JSON 字符串解码为 Python 对象
json.dumps   ----》将 Python 对象编码成 JSON 字符串

"""
import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, {'name': '王和酒杀', 'age': '21'}]
data1 = json.dumps(data,ensure_ascii=False)
print(data1)
print("data1的数据类型：",type(data1))
# data2 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
# print(data2)
print("------------------------------分割线-----------------------------------")
# json.loads
# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。

json_str = '{"name":"qiyue","age":18}'
print(type(json_str))
student = json.loads(json_str)
print("打印student：", student)
print(type(student))
















