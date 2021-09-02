# encoding:utf8

num=input().split()
n=int(num[0])
m=int(num[1])
li=[]
for i in range(n,m+1):
    if i %4==0:
        li.append(i)
for i in range(3):
    try:
        print(li[i],end=' ')
    except:
        print(-1,end=' ')