# 用dict表示学生
std1 = {'name': 'Michael', 'score': 80}


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print(self):
        print(self.name, self.score)


std2 = Student('m', 90)

std2.print()
