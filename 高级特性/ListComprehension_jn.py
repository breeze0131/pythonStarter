#  生成器生成9x9乘法表
[print('%d * %d = %d' % (x, y, x * y)) for x in range(1, 9) for y in range(1, 9)]

#  带条件
[print(x) for x in range(1, 9) if x % 2 == 0]

d = {1: 'a', 2: 'b', 3: 'c'}

[print(k, v) for k, v in d.items()]

# 练习
#
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)