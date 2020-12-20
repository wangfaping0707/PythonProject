print(type({1,2,3,4,5}))
set1={1,2,3,4,5,6}
print(len(set1))
print(1 in set1)
print(1 not in set1)
print(set1-{3,4})  #求集合的差集
print(set1&{3,4})  #求集合的交集
print(set1|{3,4,5,6,8,7})  #求集合的合集或者并集
dit={'Q':"新月打击",'W':"月之护盾",'E':"月之降临",'R':"月神冲刺"}
print(type(dit))
print(dit["Q"])
print(dit["R"])
print(dit)
print(type({}))    #空的字典，用{}来表示
print(type(set())) #空的集合，用set()来表示
print(type(()))    #空的元组，用()来表示
print(type([]))    #空的列表，用[]来表示