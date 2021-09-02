# encoding:utf8

num=input().split()
n=int(num[0])
m=int(num[1])
nums=list(map(int,input().split()))
li=[]
for i in range(len(nums)-m+1):
    res=nums[i]
    for j in range(1,m):
        res*=nums[i+j]
    li.append(res)
print(min(li),li.index(min(li))+1)