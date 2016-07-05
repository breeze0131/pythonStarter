# __str__() 用于print 打印  __repr__() 用于回显  __getattr__用于动态获得属性
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    d__repr__ = __str__

    def __getattr__(self, item):
        if item == 'score':
            return 99


std1 = Student("mm")
print(std1)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# __iter__() 想用 for ..in .. __next__() 获取下一个值

# __getitem__() 按照下标取出元素
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

# __call__() 调用某个实例的方法
