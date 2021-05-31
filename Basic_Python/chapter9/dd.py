class h():

    sex = 'male'

    def __init__(self, name, age):
        self.name = name
        self.age = age


h1 = h('wang',21)
print(h1.__dict__)

print(h1.__dir__())
print('-------------------------------------------')
h1.sex = 'male'
h1.kk = 333
print(h1.__dict__)

print(h1.__dir__())