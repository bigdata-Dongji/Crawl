# encoding:utf8

n=int(input())
li=[]
for i in range(n):
    row=list(map(int,input().split()))
    li.append(row)
li_res,li_pos=[],[]
for i in range(1,n-1):
    for j in range(1,n-1):
        if li[i-1][j]<li[i][j] and li[i+1][j]<li[i][j] and li[i][j-1]<li[i][j] and li[i][j+1]<li[i][j]:
            li_res.append(li[i][j])
            li_pos.append([i,j])
try:
    print(li_pos[li_res.index(max(li_res))][0]+1,li_pos[li_res.index(max(li_res))][1]+1)
except:
    print(-1,-1)