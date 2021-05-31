"""
要引发异常,可使用raise语句,并将一个类(必须是Exception的子类)或实例作为参数，将自动创建一个实例
类后面括号中的信息，是报错时提示的异常信息
"""
# raise Exception
# raise Exception('hyperdrive overload')

raise ArithmeticError('你好，我是算术异常')
