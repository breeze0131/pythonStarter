# ord()与chr() ord
ord('中')
chr(25991)
# 字节
x = b'ABC'
# 把字符串编码为指定bytes
'ABC'.encode('ascii')
'中文'.encode('utf-8')
# 把bytes转换为字符串
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# 计算字符串长度
len('ABC')
# 格式化 C风格

# 练习
s1 = 72
s2 = 85
r = (s2 - s1) / s2 * 100
print('%.1f%%' % r)
