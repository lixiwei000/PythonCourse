# 三目运算符
result = 'GT' if 1 > 3 else 'LT'
print(result)

func = lambda x,y : x + y
print(func(3,4))

list = map(lambda x:x*2,range(10))
for i in list:
    print(i)