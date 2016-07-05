# 类属性
class Student(object):
    name = 'Student'


std1 = Student()
print(std1.name)
# 相同名称的实例属性将屏蔽掉类属性
std1.name = 'aaa'
print(std1.name)
del std1.name
print(std1.name)
