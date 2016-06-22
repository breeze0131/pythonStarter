def move(n):
    if n==1:
        return 1
    return n * move(n-1)

t=move(8)
print(t)


def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('wang','woman')
enroll('wangchao', 'woman', 18, 'yunnan')