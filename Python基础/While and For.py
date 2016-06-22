y=range(100)
t=0
for x in y:
    t=t+x
print(t)

if t>500:
    print("正确")
else:
    print("错误")

while t>0:
    t=t-100
    print(t)
