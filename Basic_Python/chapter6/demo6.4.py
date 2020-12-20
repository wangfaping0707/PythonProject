def change(n):
    n[0] = "wumeifang"
names = ["大熊", "胖虎", "杜伊"]
print("列表之前：", names)
change(names[:])
print("列表之后：", names)
