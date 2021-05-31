# author ：wang123 
# 创建时间 ：2021/1/24 15:1
open('log.txt')


# data的目录下可能有各种数据格式结尾的文件（ .txt .csv  .xml ,config)
# 如果一个函数的参数既有位置参数，又有关键字参数，那么关键字参数要放到最后，不然函数回报错
def data_dir(file_path="d:/data", file_name=None):
	print(file_path)
	print(file_name)


data_dir('text.txt')
print("---------------------分割线--------------------------------")
data_dir(file_name='text.txt')


