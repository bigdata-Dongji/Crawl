#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

#source code demo
def main():
    s=input()
    num_li=re.findall('(\d+)',s)
    add=0 # 递增次数
    minus=0 # 递减次数
    than=len(num_li)-1 # 比较次数
    for i in range(1,len(num_li)):
        if int(num_li[i])>int(num_li[i-1]):
            add+=1
        elif int(num_li[i])<int(num_li[i-1]):
            minus+=1
    if than==add:
        print('INC')
    elif than==minus:
        print('DEC')
    else:
        print('NUL')

if __name__ == '__main__':
    main()