
print("hello\nworld")

print("we love \\n you")

print(ord('A'))
print("---------------------------------")

# 集合是由花括号包裹的表现形式，而且大体也拥有部分序列的特性，当然集合与序列最大的不同就是，集合是无序的，也就是说我
# 们不能通过序号去得到相应的集合元素。那怎么得到集合中的元素呢，这个之后再说，我们先来看集合的一些特性

set1 = { 10, 1, 2, 3,4, 5}
set2 = {4, 5, 6, 8, 9, 7, }
print(set1)
print('两个集合的交集：', set1 & set2)
print("两个集合的并集", set1 | set2)
print("两个集合的差集", set1 - set2)

list1 = [1,2,3]
list2 = [4,5,6,7,1]
print(list1 + list2)
b=1
b += b >= 1
print(b)

print(ord("王"))