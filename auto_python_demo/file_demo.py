import io

# python读取文件中文乱码，在open后加encoding可以解决
# f = open("somefile.txt", encoding="utf-8")
#
# text = f.read()
# print(text, type(text))

# 写文件

# with open("somefile.txt", 'a+', encoding='utf-8') as f:
#     f.write("成老板的美丽-翠红")


# 读文件
with open("somefile.txt", encoding='utf-8') as f1:
    print(f1.read())
