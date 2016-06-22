# map(fx(), []) 批量处理队列
# filter(fx(), []) 过滤队列
# sorted([])   排序队列

def Triple(x):
    return x * x

r= map(Triple, [1, 3, 5, 7, 9])
print(list(r))


def left(x):
    if x>0:
        return True
    elif x<=0:
        return False

l= filter(left,[-1, 0, 1, 3])
print(list(l))

Bigger=sorted([-22, 13, 2, 0, -11], key= abs)
print(Bigger)