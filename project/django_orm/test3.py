import random
li=[]
for i in range(20):
    li.append(random.randint(0,99))
print('生成的20个数:',li)
max_list=[]
for i in range(5):
    max_num=0
    for j in li:
        if j>max_num:
            max_num=j
    li.remove(max_num)
    max_list.append(max_num)
li=tuple(li)
max_list=tuple(max_list)
print('剔除最大5个数后的元组：',li)
print('剔除掉的最大5个数：',max_list)
