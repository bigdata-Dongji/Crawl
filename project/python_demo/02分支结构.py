# encoding:utf8
if 5:
    print(6)

if 0: # 0作为表达式是不合法，所以不会执行
    print(1)

if [1,2,3]: # 列表也可作为表达式
    print('list')

# 三元表达式
print(1) if 1>2 else print(2) # 2
a=0 if 1>2 else 10
print(a) # 10
