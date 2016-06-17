from collections import Iterable

#  迭代列表和元组之外还能迭代dict
d = {1: 1, 2: 2, 3: 3, 4: 4}
for k in d:  # 迭代key
    print(k)
for v in d.values():  # 迭代value
    print(v)
for k, v in d.items():  # 迭代k,v
    print(k, v)

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

#  按下标迭代使用enumerate
for i, v in enumerate([1, 2, 3, 4]):
    print(i, v)
