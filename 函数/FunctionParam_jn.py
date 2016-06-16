# 默认参数


def test(a, b, c=10):
    print(a, b, c)


# 默认参数的坑,不要使用可变的对象作为默认参数
def test2(c=[]):
    c.append('end')
    print(c)


test2()
test2()  # 打印出 ['end', 'end']


# 解决方案使用None这样的不可变对象
def test3(c=None):
    if c is None:
        c = []
    c.append('end')
    print(c)


# 变长参数 ,变长参数相当于把多个参数变成一个tuple
def var_args(*args):
    for arg in args:
        print(arg)


var_args(1, 2, 3, 4)
var_args(*[1, 2, 3, 4])  # 对于list和tuple可以加*来表示为变长参数
var_args(*(1, 2, 3, 4))


# 关键字参数，关键字参数相当于把参数变成dict

def kv_args(a, b, **c):
    print(a, b, c)


kv_args(1, 2, str='hello')
extra = {'str': 'hello', 'age': 18}
kv_args(1, 2, **extra)


# 限制关键字

def explict_kv_args(a, b, *, strs):
    print(a, b, strs)


explict_kv_args(1, 2, strs='111')

# 各种组合


