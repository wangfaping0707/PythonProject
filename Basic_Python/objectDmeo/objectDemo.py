class Employee:
    """所有员工的基类"""
    # empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, "Salary", self.salary)

# "创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 20000)
# "创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 50000)

# 使用点号 . 来访问对象的属性。使用如下类的名称访问类变量
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d "%Employee.empCount)

# 你可以添加，删除，修改类的属性
emp1.age = 26
print("员工emp1新增的属性->年龄：",emp1.age)
emp1.age = 29
print("员工emp1新增的属性->年龄修改之后：",emp1.age)


"""
1、实例的__dict__仅存储与该实例相关的实例属性，正是因为实例的__dict__属性，每个实例的实例属性才会互不影响。
   类的__dict__存储  所有实例  共享的  变量和函数(类属性，方法等)，类的__dict__并不包含其父类的属性
2、dir()是Python提供的一个API函数，dir()函数会自动寻找一个对象的所有属性(包括从父类中继承的属性)。
​  一个实例的__dict__属性仅仅是那个实例的实例属性的集合，并不包含该实例的所有有效属性。所以如果想获取一个对象所有有效属性，应使用dir()。
"""
print("实例emp1所拥有的属性：",emp1.__dict__)
print("类Empoyee所拥有的属性：",Employee.__dict__)

"""
可以使用以下函数的方式来访问属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
"""
print("使用hasattr方法来判断emp1是否有age属性:",hasattr(emp1,'age'))
print("使用getattr方法来访问emp1的属性:",getattr(emp1,'age'))
# 给对象emp1添加一个属性favorite
setattr(emp1,'favorite','movie')
print("实例emp1所拥有的属性：",emp1.__dict__)
# 删除实例emp1新增的属性favorite
delattr(emp1,'favorite')
print("实例emp1所拥有的属性：",emp1.__dict__)

"""
Python内置类属性
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
"""
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)











