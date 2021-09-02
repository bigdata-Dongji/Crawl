#!/usr/bin/python
#-*- coding:utf-8 -*-



#source code demo
def main():
    people_num=int(input())
    scores=input().split()
    scores=list(map(int,scores))
    A,B,C,D=0,0,0,0
    for s in scores:
        if 85<=s and s<=100:
            A+=1
        elif 75<=s and s<=84:
            B+=1
        elif 60<=s and s<=74:
            C+=1
        elif 0<=s and s<=59:
            D+=1
    print('A',A)
    print('B',B)
    print('C',C)
    print('D',D)

if __name__ == '__main__':
    main()