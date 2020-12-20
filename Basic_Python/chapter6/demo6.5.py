x = 9
print(vars()['x'])
print('var()的类型：', type(vars()))

external = 'berry'


def combine(parameter):
    print(parameter + external)


combine('Shurb')


y = 3
parameter = 'Hello World'


def combin(parameter):
    print(parameter, globals()['parameter'])


combin('kavin')

a = 13
def change_global():
    global a
    a += 2
    print(a)

change_global()