"""
Python 正则表达式 : 正则表达式是一个特殊的字符序列，它能帮助你方便的检查一个字符串是否与某种模式匹配
re 模块使 Python 语言拥有全部的正则表达式功能
（Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句）
compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。
本章节主要介绍Python中常用的正则表达式处理函数。
"""

"""
findall
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。
语法格式为：findall(string[, pos[, endpos]])
参数：string : 待匹配的字符串  pos : 可选参数，指定字符串的起始位置，默认为 0  endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。 
查找字符串中的所有数字：                                 
"""
import re
# z在字符串a中找到所有Python
a = "C654C++56Java57C#786Python009Javascript5678Python"

print(re.findall("\\d", a))

s = "abc,acc,adc,aec,afc,ahc"
regex1 = "a[cf]c"
print(re.findall(regex1, s))
regex2 = "a[^cf]c"
print(re.findall(regex2,s))

# ^匹配字符串的开头     [^...]  :  不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。

str = "python 1111java678php"

regex3 = "[a-z]{3,6}?"

print("正则表达式数量词练习：", re.findall(regex3, str))

str1 = "pytho0python844pythonn434pythonnnn"

regex4 = "python?"

# *号表示匹配前面的字符0次或无限多次
# +号表示匹配前面的字符1次或无限多次
# ？号表示匹配前面的字符0次或1次

print(re.findall(regex4, str1))


str2 = "PythonC#Java454Php"

regex5 = "c#"

print(re.findall(regex5, str2, re.I))
print("-------------------------------------------")

"""
(.*）”得到的是只有一个元素的列表，里面是很长的字符串
（.*？）”则是得到包含几个元素的列表，每个元素直接对应原来文本中不同的位置匹配的项
例如：十个人肩并肩的并排走着，使用“（.*）”的取到了从第一个人到最后一个人的所有东西在一起，后者则是分别取下了十个人的东西
前者成为贪婪模式，获取最长的满足条件的字符串
后者称为非贪婪模式，获取最短的能满足条件的字符串
"""
regex6 = ".*"
regex7 = ".*?"
regex8 = "a(.*)b"
regex9 = "a(.*?)b"
str3 = "a123ba123b"
rt = re.findall(regex6, str3)
rt1 = re.findall(regex7, str3)
rt2 = re.findall(regex8, str3)
rt3 = re.findall(regex9, str3)
print(rt)
print(rt1)
print(rt2)
print(rt3)

