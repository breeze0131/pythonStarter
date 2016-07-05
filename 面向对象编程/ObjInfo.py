import types

# type() 获取类型
type(123)
print(type(123) == int)
type(abs) == types.BuiltinFunctionType


def fn():
    pass


type(fn) == types.FunctionType
type(lambda x, y: x + y) == types.LambdaType


# isinstance()
class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Huskey(Dog):
    pass


a = Animal()
d = Dog()
c = Cat()
h = Huskey()

print(isinstance(d, Dog))
print(isinstance(a, Dog))
print(isinstance(d, Animal))
print(isinstance(h, Huskey))
print(isinstance(h, Dog))
print(isinstance(h, Animal))


# dir()
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
class MyDoc(Dog):
    def __len__(self):
        return 100

    def __init__(self):
        self.x = 9


m = MyDoc()
print(dir('ABC'))
print(len(m))
print(getattr(m, 'x'))
print(hasattr(m, 'x'))
setattr(m, 'x', 10)
print(m.x)
