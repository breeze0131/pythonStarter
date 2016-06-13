# List
fruits = ['apple', 'banana', 'peach']
# 下标访问
fruits[0]
# 倒数第几个元素
fruits[-1]
# 增加元素
fruits.append('pear')
# 删除末尾元素
fruits.pop()
# 在指定位置插入,在指定位置删除
fruits.insert(1, 'a')
fruits.pop(1)
# 替换某个位置的元素
fruits[1] = 'a'
# List 嵌套List
[['a', 'b'], 'c']

# 元组 元组初始化后不能修改，所以是不可变的
t = (1, 2)
# 空元祖
t2 = ()
# 只有一个元素的元组比较特殊
t3 = (1,)


# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

