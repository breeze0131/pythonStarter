# 类和实例 类是模板，实例是由模板创建出的对象



# 括号里表示继承自那个类
class Student(object):
    # 构造方法
    def __init__(self, name, score):
        self.name = name
        self.score = score
    #封装数据
    def printScore(self):
        print(self.score)


# std1是一个实例
std1 = Student("m", 90)
# 可以给实例自由绑定属性
std1.age = 90
print(std1.age)
