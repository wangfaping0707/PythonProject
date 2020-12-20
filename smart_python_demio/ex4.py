# 总共有汽车100辆
cars = 100
# 一辆汽车可做4个人
space_in_a_car = 4.0
# 有司机30个人
drivers = 30
# 乘客90个人
passengers = 90
# 没有被驾驶的汽车数量
cars_not_driven = cars - drivers
# 已被驾驶的汽车数量
cars_driven = drivers
# 已被使用的汽车空间
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆汽车的载客数
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
