from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'set_age', 'set_score', 'score')


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


std1 = Student()
std1.set_age = MethodType(set_age, std1)
std1.set_age(25)
print(std1.age)
# 给一个实例绑定的方法，对另一个实例是不起作用
std2 = Student()


# std2.set_age(25)


# 为了给所有实例绑定方法，可以把方法绑定在类上
def set_score(self, score):
    self.score = score


Student.set_score = set_score
std2.set_score(20)
print(std2.score)
