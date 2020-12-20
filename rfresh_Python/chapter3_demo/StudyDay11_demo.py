"""
re.sub的功能:
re是regular expression的所写，表示正则表达式   sub是substitute的所写，表示替换；
re.sub是个正则表达式方面的函数，用来实现通过正则表达式，实现比普通字符串的replace更加强大的替换功能；
举个最简单的例子：如果输入字符串是：inputStr = "hello 111 world 111"
那么你可以通过:
replacedStr = inputStr.replace("111", "222")
去换成:       "hello 222 world 222"
但是，如果输入字符串是： inputStr = "hello 123 world 456"   而你是想把123和456，都换成222
那么就没法直接通过字符串的replace达到这一目的了。就需要借助于re.sub，通过正则表达式，来实现这种相对复杂的字符串的替换：
replacedStr = re.sub("\d+", "222", inputStr)
对于输入的一个字符串，利用正则表达式（的强大的字符串处理功能），去实现（相对复杂的）字符串替换处理，然后返回被替换后的字符串
其中re.sub还支持各种参数，比如count指定要替换的个数等等。
下面就是来详细解释其各个参数的含义。
re.sub的各个参数的详细解释:   re.sub共有五个参数。
其中三个必选参数：pattern, repl, string
两个可选参数：count, flags
"""
import re

language = "Python44C#45Java66C#767HTML676C#070Javascript7876Ruby"
r = re.sub("C#", "Go", language,1)
print(language)
print(r)

print("------------------------------------分割线----------------------")
"""
python中的group方法: group（）在正则表达式中用于获取分段截获的字符串，解释如下代码：
可以看出，正则表达式按照数字-字母-数字的顺序来获取相应字符串，
那么分别就是“数字（group（1））--字母（group（2））--数字（group（3））”的对应关系，
其中，group（0）和group（）效果相同，均为获取取得的字符串整体。
"""
a = "123abc-456"
res = re.search("([0-9]*)([a-z]*)([0-9]*)", a)
print("返回的是一个对象：", res)
print("res的类型是：",type(res))
print(res.group(0))  # 123abc456,返回整体
print(res.group(1))  # 123
print(res.group(2))  # abc
print(res.group(3))  # 456
print(res.group(1, 2, 3))  # 返回结果是一个元组
print(res.groups())
print("------------------------------------分割线----------------------")

"""
re.search方法:
re.search 扫描整个字符串并返回第一个成功的匹配。
函数语法：re.search(pattern, string, flags=0)
函数参数说明：pattern  匹配的正则表达式    string	 要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法：
group(num=0) 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
"""
print(re.search('www', 'www.baidu.www.com').span())         # 在起始位置匹配
print(re.search('com', 'www.baidu.www.com').span())         # 不在起始位置匹配
print("------------------------------------分割线----------------------")
a = r"umji"
match = re.search(a,"umji isbest umji inworld")
if match:
    print(match.group())  # group  以str形式返回对象中match的元素
    print(match.groups())
    print(match.start())  # start  返回开始位置  表示前面有多少个元素
    print(match.end())    # end    返回结束位置
    print(match.span())   # span   以tuple形式返回范围
    print(type(match.group()))
print("------------------------------------分割线----------------------")

"""
解析:  首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，
也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
(.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
(.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的
因为只有匹配结果中只有两组，所以如果填 3 时会报错
"""
line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

print("------------------------------------分割线----------------------")




















