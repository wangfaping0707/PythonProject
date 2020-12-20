def print_params(*params):
    print(params)


print_params('hello', 1, 2, 3)

print('----------------------------------------------------------')


def print_params_2(title, *patams):
    print(title)
    print(patams)


print_params_2('loving_story:', 1, 2, 3)

print_params_2('nothing:')


def in_the_middle(x, *y, z):
    print(x, y, z)


in_the_middle(1, 2, 3, 4, 5, 6, 7, z=8)


# print_params_2('Hm........', something=42)


def doSomething(**params):
    print(params)


doSomething(x=1, y=2, z='3')
