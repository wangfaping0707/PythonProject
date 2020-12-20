dict = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': '0'}
print(dict.items())
print(len(dict.items()))
print(('spam', '0') in dict.items())

print(dict.keys())
print(dict.values())

dict1 = {'x': '1', 'y': '2'}
print(dict1.pop('x'))
print(dict1)

print(dict.popitem())
print(dict)

d = {}
print(d)
d.setdefault('name', 'N/A')
print("setdefault方法之后的打印：",d)
d.setdefault('name', '11')
print(d)
d['name'] = "Gumny"
d.setdefault('name', 'N/A')
print(d)


import chapter4