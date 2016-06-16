import math


# 空函数
def nop():
    pass


# 检查参数类型
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值，实际返回的是元组


def move(x, y, step, angle=0):
    nx = x + step * math.sin(angle)
    ny = y + step * math.cos(angle)
    return nx, ny


x, y = move(1, 1, 10, 90)
print(x, y)
r = move(1, 1, 10, 90)
print(r)


# 练习
#
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#
# ax2 + bx + c = 0
def quadratic(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    if delta < 0:
        return None
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))