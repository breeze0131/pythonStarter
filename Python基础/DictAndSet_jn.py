# dict 跟java的map差不多 两种初始化方法
scores = {'A': 3, 'B': 2, 'C': 1}
print(scores['A'])
d = {}
d['A'] = 3

# key不存在时会报错
# scores['d']
# 判断key是否存在
print('A' in d)
# 使用get 不存在则返回none 或赋默认值
d.get('B')
d.get('B', 0)
# pop 删除 key
d.pop('A')
# dict 的key应当是不可变的

# set
s = {1, 1, 1, 2, 2, 3}
s.add(4)
s.remove(2)
print(s)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 | s2)
print(s1 & s2)
