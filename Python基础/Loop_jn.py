# for .. in ..
nums = [1, 2, 3, 4]
for num in nums:
    print(num)
# range()
list(range(2))

# while
sumi = 0
i = 1
while i < 101:
    sumi += i
    i += 1
print(sumi)

# 练习
#
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,' + name)
