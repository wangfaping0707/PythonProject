def hello1(greeting, name):
    print("{},{}!".format(greeting, name))


def hello2(name, greeting):
    print("{},{}!".format(greeting, name))


hello1("hello", 'world')
hello2("hello", 'world')

hello1(name='Gumby', greeting='Hi')

print("------------------------------------------------------")


def Hello3(greeting="Hi", name="the world"):
    print("{},{}".format(greeting, name))


Hello3()
Hello3("Hello", "fang")
Hello3(greeting="do it now")
Hello3(name="lazy")

print("------------------------------------------------------")


def hello4(name, greeting='Hello', punctuation='!'):
    print("{},{},{}".format(greeting, name, punctuation))


hello4('wu')
hello4('wu', 'love')
hello4('wu', 'love', '***')
hello4('wumeifang', greeting='makesloving')
