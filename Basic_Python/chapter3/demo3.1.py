from math import pi

format = "Hello,%s.%s enough for ya?"
values = ('world', 'Hot')
print(format % values)

str = "{name} is approximately {value:.2f}.".format(value=pi, name="π")

str1 = "{name} is approximately {value}".format(value=pi, name="π")
print(str)
print(str1)

str3 = "{foo} {} {bar} {}  {}".format(1, 2, 5, bar=7, foo=13)
print(str3)

fullname = ["Alfred","Smoketoomuch"]
str4 = "Mr {name[1]}".format(name=fullname)
print(str4)

print("{pi!s}  {pi!r}  {pi!a}".format(pi="π"))

print("The number is {num:d}".format(num=42))
print("The number is {num:f}".format(num=42))
print("The number is {num:b}".format(num=42))
print("The number is {num:c}".format(num=42))
print("The number is {num:e}".format(num=42))
print("The number is {num:E}".format(num=42))
print("The number is {num:F}".format(num=42))
print("The number is {num:s}".format(num="42g"))
print("The number is {num:%}".format(num=42))

print("{num:10}".format(num=3))
print("{num:10}".format(num="Bob"))

print("Pi day is {pi}".format(pi=pi))
print("Pi day is {pi:f}".format(pi=pi))
print("Pi day is {pi:.3f}".format(pi=pi))

















