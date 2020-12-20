a=[1,2,3,4,5,6]
b=a
a[0]='frseh_start'
print(a)
print(b)
str="Hello"
str1=str+"This a world"
print(id(str))
print(id(str1))
print("--------------分割线-----------")
print(id(a))
print(id(b))
a={1,2,3}
b={2,1,3}
print(a==b)
print(a is b)
print("--------------分割线-----------")
print(isinstance(a,list))
print(isinstance(a,set))
print(isinstance(a,dict))
