# 代码块的嵌套
name = input("What's your name:")
if name.endswith("Gumby"):
    if name.startswith("Mr."):
        print("Hello,", name)
    elif name.startswith("Mrs."):
        print("Hello,", name)
    else:
        print("Hello,Gumby")
else:
    print("Hello,stranger")
