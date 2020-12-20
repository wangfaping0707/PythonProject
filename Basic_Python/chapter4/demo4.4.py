phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phonebook['Beth'])

print("Cecil's phone number is {Cecil}.".format_map(phonebook))


items = [('name', 'Gunby',), ('age', '42'), ('love', 'yiu')]
d = dict(items)
print(d)
print(d['love'])

d1 = dict(张飞='丈八蛇矛', 曹操='青钢剑', 关羽='青龙偃月刀')
print(d1)
print(len(d1))
d1['吕布']='方天画戟'
d1['黄忠']='麒麟弓'
print(d1)
del (d1['黄忠'])
print(d1)
print('吕布' in  d1)
