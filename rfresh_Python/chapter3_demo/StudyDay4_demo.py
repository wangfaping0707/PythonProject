"""
Python dir() 函数
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

dir()函数的返回值：返回模块的属性列表。
"""

a = 3
#  获得当前模块的属性列表
infos = dir()

print("Python中的模块的属性列表：", infos)

print("name:"+ __name__)
print("doc:"+ __doc__)
print("package:", __package__)
print("file:"+__file__)
