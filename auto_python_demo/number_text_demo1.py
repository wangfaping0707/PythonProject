with open('number.txt',encoding='utf-8') as f:
    lines = f.readlines()
    print(lines, type(lines))
    print(lines[0])


print("---------------------------------风格线---------------------")

with open('number.txt', encoding='utf-8') as f1:
    for line in f1:
        print(line)
