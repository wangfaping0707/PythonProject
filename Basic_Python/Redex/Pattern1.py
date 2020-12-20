import re

a = 'python 1111java768php'

r1 = re.findall("[a-z]{3,6}", a)
r2 = re.findall("[a-z]{3,6}?", a)

print("贪婪模式：", r1)
print("非贪婪模式：", r2)

b = "pytho0python3636pythonnn2323pythonn2"

# * 匹配0次或者无数次
# + 匹配1次或者无数次
# ? 匹配0次或者1次
r3 = re.findall("python*", b)
r4 = re.findall("python+", b)
r5 = re.findall("python?", b)
print("*数量词匹配：", r3)
print("+数量词匹配：", r4)
print("?数量词匹配：", r5)

c = "PythonC#PhpJava34javascript"

r6 = re.findall("c#", c)
r7 = re.findall("c#", c, re.I)

print(r6)
print(r7)
