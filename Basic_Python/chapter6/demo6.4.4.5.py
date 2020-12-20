# 函数一
def story(**kwd):
    return "Once upon a time,there was a {job} called {name}".format_map(kwd)


print("方式一：", story(job='king', name='Gumby'))

print("方式二：", story(name='Sir Robin', job='brave knight'))

params = {'job': 'language', 'name': 'Python'}
print("方式三：", story(**params))

del params['job']
print("方式四：", story(job="stroke of genius", **params))


# 函数二
def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


print("power的值:", power(2, 3))
print("power的值:", power(3, 3))
print("power的值:", power(x=4,y=2))

params=(5,)*2
print("参数params的值：",params)
print(power(*params))

print("参数params的值：",power(3,3,'Hello World'))
































