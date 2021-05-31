import json
import requests

"""
字典的序列化和反序列化
"""

dict1 = {"a": 1, "b": 2}

print("序列化之前的数据类型：", type(dict1))

# 序列化：dict---》str
str_dict = json.dumps(dict1)
print(str_dict)
print("序列化之后的数据类型：", type(str_dict))

# 反序列化：str-->dict

dict_str = json.loads(str_dict)
print(dict_str)

print("反序列化之后的数据类型：", type(dict_str))
print("-----------------------------------------------分割线--------------------------------------------------")

"""
列表的序列化和反序列化
"""

list1 = ['ya2', 'admin', 'wee']
# 列表进行序列化
print("列表序列化之前的打印：", list1)
str_list1 = json.dumps(list1)
print("列表序列化之后的打印：", str_list1)
print("列表序列化后的数据类型：", type(str_list1))
# 列表进行反序列化
list2 = json.loads(str_list1)
print("列表反序列化之后的打印：", list2)
print("列表反序列化后的数据类型：", type(list2))
print("--------------------------------分割线---------------------------")
"""
元组的序列化和反序列化的过程
"""

tuple1 = ("a", "b", "c", "d")
print("tuple序列化之前的数据类型：", type(tuple1))

str_tuple=json.dumps(tuple1)

print("元组序列化之后的打印", str_tuple)
print("序列化之后的数据类型", type(str_tuple))

tuple2 = json.loads(str_tuple)
print("元组反序列化之后的打印", tuple2)
print("序列化之后的数据类型", type(tuple2))
