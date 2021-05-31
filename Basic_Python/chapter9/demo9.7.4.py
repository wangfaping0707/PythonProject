def count_down(n):
    while n >= 0:
        newn = yield n
        print('newn', newn)
        if newn:
            print('if')
            n = newn
            print('n =', n)
        else:
            n -= 1


cd = count_down(5)
for i in cd:
    print(i, ',')
    if i == 5:
        cd.send(3)
