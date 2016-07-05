# 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


std1 = Student('n', 200)
std1.set_name('ll')
