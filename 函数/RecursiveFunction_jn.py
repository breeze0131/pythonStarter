# 递归求阶乘 这种方式可能会导致调用栈过深产生栈溢出
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# 尾递归方式 尾递归就是某个分支调用自己，可以被编译器优化为循环
def tail_fact(n, product=1):
    if n == 0:
        return product
    else:
        return tail_fact(n - 1, product * n)

print(tail_fact(3))


# 练习
#
# 汉诺塔的移动可以用递归函数非常简单地实现。
#
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
# def move(n, a, b, c):
    