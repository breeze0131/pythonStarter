from functools import reduce

# 变量可以指向函数
o = abs


# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def myAdd(x, y, f):  # 这里的参数f是一个函数所以add是一个高阶函数
    return f(x) + f(y)


print(myAdd(1, -1, abs))
# map (f,Iterable) 对Iterable 中的每一个对象应用函数f
print(list(map(abs, [1, -1, -21])))

# reduce (f,Iterable) f接受两个参数，对Iterable中每两个对象应用f
print((reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])))


# map reduce
def f1(x):
    return x + x


def f2(x, y):
    return x + y


print(reduce(f2, list(map(f1, "abc"))))


# 练习
#
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].capitalize() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    if not isinstance(L, list):
        raise TypeError("类型错误！！")
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

# 懒得写了


# filter() 过滤
# 生成素数 奇数数列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选函数

def _not_divisible(n):
    return lambda x: x % n > 0


# 生成函数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 练习
#
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

def is_palindrome(n):
    l = len(str(n))
    s = str(n)
    for i in range(0, int((l + 1) / 2)):
        if s[i] != s[l - 1 - i]:
            return False
    return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
