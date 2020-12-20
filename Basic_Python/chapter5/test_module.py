
import package_name.varible_name

print("*********************************test_module*****************************************")

print("name:"+ (__name__ or "当前模块没有名字"))

print("doc:" + (__doc__ or "当前模块没有注释！！！"))

print("package:" + (__package__ or "当前模块没有所属的包"))

print("file:" + (__file__ or "当前模块没有所处的路径"))