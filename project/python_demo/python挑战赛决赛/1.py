#!/usr/bin/python
#-*- coding:utf-8 -*-



#source code demo
def main():
    num = int(input())
    d_sum=0 # 按策略D的话菜品总价
    meat=0 # 荤菜数量
    vege=0 # 素菜数量
    for i in range(num):
        s = input().split()
        s_num = float(s[1])
        price=float(s[2])
        if s[0]=='M':
            meat+=s_num
            d_sum+=s_num/100*price
        elif s[0]=='V':
            vege+=s_num
            d_sum += s_num/100*price
    general_price = input().split()
    t_sum = (meat / 100*float(general_price[0]))+(vege/100*float(general_price[1]))

    if d_sum < t_sum:
        print('D')
    elif t_sum < d_sum:
        print('T')
    else:
        print('=')


if __name__ == '__main__':
    main()
