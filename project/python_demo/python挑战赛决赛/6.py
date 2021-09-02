#!/usr/bin/python
#-*- coding:utf-8 -*-



#source code demo
def main():
    info=input().split()
    surplus=float(info[1])-float(info[2]) # 剩余容量
    num=int(input())
    li=[] # 存储单位车厢载重和车厢数量
    for i in range(num):
        s=input().split()
        li.append([float(s[0]),float(s[1])])
    li=sorted(li)
    max_num=0 # 输出的最多车载数量
    for i in li:

        if i[0]*i[1]<surplus:
            max_num+=i[1]
            surplus-=i[0]*i[1]
        else:
            for j in range(int((i[1])-1),0,-1):
                if i[0]*j<surplus:
                    max_num+=j
                    surplus -=i[0]*j
    print(str(info[0]),'+'+str(int(max_num)-1))
if __name__ == '__main__':
    main()