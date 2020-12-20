from math import pi

print("{:010.2f}".format(pi))

# 要指定左对齐、右对齐和居中，可分别使用<、>和^
print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi))

print("{str:$^15}".format(str="WIN BIG"))
print("{num:*^10.2f}".format(num= -pi))
print("{num:*<10.2f}".format(num= -pi))
print("{num:*>10.2f}".format(num= -pi))
print("{num:*=10.2f}".format(num= -pi))

print("{num:<+10.2f}".format(num= pi))
print("{num:^+10.2f}".format(num= pi))
print("{num:>+10.2f}".format(num= pi))