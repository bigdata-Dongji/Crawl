# encoding:utf8
g=(i for i in range(10)) # 如果外层是[]就是列表推导式，如果是()就是生成器对象
print(g) # <generator object <genexpr> at 0x0000022F13C0D6C8>
print(g.__next__()) # 返回下一个元素，返回0
print(g.__next__()) # 返回1
print(next(g)) # 返回2
tuple_g=tuple(g)
print(tuple_g) # (3, 4, 5, 6, 7, 8, 9)
t=tuple(g)
print(t) # 返回()，因为生成器对象已遍历结束，没有元素了
g=(i for i in range(10)) # 重新构造生成器
print(g)
print(list(g)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('-'*50)
from collections import Iterable
print(isinstance('abc',Iterable)) # 判断是否可迭代
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))