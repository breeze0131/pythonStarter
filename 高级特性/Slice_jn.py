# 前三个元素
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst[:3])

# 后三个元素

print(lst[-3:])

# 配合range

lst2 = list(range(100))
print(lst2[:10])
print(lst2[:10:2])  # 前10个每2个取一个
print(lst2[::5])  # 每5个取一个
print(lst2[::])  # 复制列表

(1, 2, 3, 4, 5)[:3]
'ABCDEDF'[:5]  # tuple 和字符串也可以


