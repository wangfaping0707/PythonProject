
fibs = [0, 1]
num=int(input("Enter your number:",))

print(type(num))
for i in range(num):
    fibs.append(fibs[-2] + fibs[-1])

print(fibs)





