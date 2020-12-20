# 导入正则表达式模块
import re

a = "C|C#|Java|C++|Python|Javascript|python|Python1.1"

result = re.findall("Python", a)

if len(result) > 0:
    print("字符串中包含Python")
else:
    print("对不起，没有匹配到对应的字符串")

print(result)

print("-------------------------------------------------")

b = "C9C#8Java7C++6Python5Javascript1python3Python0"

result2 = re.findall("\d",b)

print(result2)

result2.reverse()

print("按相反顺序排列列表中的元素:",result2)

result2.sort()

print("列表中的元素按大小排序：:", result2)






















