#  跟列表生成器相比把[] 换成()

g = (x * x for x in range(10))


#  使用yield

# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


# 练习
#
# 杨辉三角定义如下：
def triangles():
    l0 = [1]
    l1 = [1, 1]
    yield l0
    yield l1
    while True:
        l1 = [1] + [l1[i] + l1[i + 1] for i in range(len(l1)-1)] + [1]
        yield l1


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break
