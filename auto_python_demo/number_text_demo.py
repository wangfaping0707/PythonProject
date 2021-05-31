with open("number.txt") as f:
    while True:
        # 循环遍历每个字符
        # char = f.read(1)
        # if not char: break
        # print("打印读取的字符：", char)

        #  以行为单位来遍历
        line = f.readline()
        if not line: break
        print("打印读取的字符：", line)