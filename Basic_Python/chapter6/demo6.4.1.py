storage = {}
storage['first'] = {}
storage['second'] = {}
storage['third'] = {}
print("打印变化之前的字典：", storage)

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['second']['Lie'] = [me]
storage['third']['Hetland'] = [me]

print("打印变化之后的字典：", storage)

print(storage['first'])

print("------------------------------------------------------------------------------")
d = {'age': 42, 'sex': 'male'}
print("字典d变化之前：", d)

print("键age对应的values：",d.setdefault('age', 'N/A'))
print("字典d变化之后1：", d)
print("键name对应的values：",d.setdefault('name', '柳思域'))
print("字典d变化之后2：", d)