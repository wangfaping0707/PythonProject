# 迭代时获取索引
strings = ['hello', 'i', 'love', 'you', '520', '1314', 'love']
for string in strings:
    if 'love' in string:
        index = strings.index('love')
        print(index)
        strings[index] = '[censored]'
print(strings)

num = ['a', 'c', 'ac', 'acd', 'vdac', 'sdac', 'we', 'w23']
for index, string in enumerate(num):
    if 'ac' in string:
        num[index] = '[censored]'

print(num)
