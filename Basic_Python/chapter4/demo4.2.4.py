# 字典方法
# 1、clear：方法clear删除所有的字典项，这种操作是就地执行(就像 list.sort一样)，因此什么都不返回(或者说返回None)
d = {}
d["name"] = 'Gumby'
d["age"] = 42
print(d)
returned_value = d.clear()
print(d)
print(returned_value)
print('----------------------------------------------------------------')

# 2、方法copy返回一个新字典，其包含的键-值对与原来的字典相同  浅复制
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
print(y)

y['username'] = 'mlh'

print(y['machines'])

y['machines'].remove('bar')

print(y)

print(x)
print('----------------------------------------------------------------')
from copy import deepcopy

d = {}
d["names"] = ['Alfred', 'Bertand']
d['age'] = '31'
print(d)
c = d.copy()
c["color"] = 'red'
print(c)
print(d)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
dc = deepcopy(d)

print(dc)

print('***************************************')
d['names'].append('Clive')
c['age'] = '29'
print(d)
print(c)
print(dc)
