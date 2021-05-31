import time


def decorator(func):
	def wrapper(*args):
		print(func, time.time())
		func(*args)

	return wrapper


@decorator
def f(func_name):
	print("This is a function named"+"  "+func_name)
	# print(time.time())


@decorator
def f1(func_name1, func_name2):
	print("This is a function names" + " " + func_name1)
	print("This is a  function named" + " " + func_name2)


f("test_name")
f1("test_name1", "test_name2")

# str = "admin"
# str1 = str.replace()
