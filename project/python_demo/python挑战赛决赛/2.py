#!/usr/bin/python
#-*- coding:utf-8 -*-



#source code demo
def main():
    num=int(input())
    li=input().split()
    li=list(map(int,li))
    for i in range(num):
        if li[i]**3 >sum(li):
            print(li[i],end=' ')

    exit()

if __name__ == '__main__':
    main()