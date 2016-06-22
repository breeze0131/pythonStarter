import functools

# 函数的名字
print(abs.__name__)


def log(func):
    def wrapper(*args, **kw):
        for arg in args:
            print(arg)
        for k, v in kw.items():
            print(k, v)
        print(func.__name__)

    return wrapper


@log
def my(*args, **kv):
    print()


my(1, 2, 3, 4, city='hello')


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def aspect(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call")
        func(*args, **kw)
        print("end call")

    return wrapper


@aspect
def hello():
    print('hello')
hello()

# 再思考一下能否写出一个@log的decorator，使它既支持：
#
# @log
# def f():
#     pass
# 又支持：
#
# @log('execute')
# def f():
#     pass

