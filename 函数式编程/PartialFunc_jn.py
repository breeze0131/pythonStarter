import functools

# 偏函数 用于固定某个参数

int2 = functools.partial(int, base=2)
print(int2('1111'))
