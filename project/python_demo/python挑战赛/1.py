# encoding:utf8
'''
Creation time: 2020/11/27 8:37 
Update time:
Purpose:
'''

'''
计算1到M (含M)之间的合数数量，输出其值。
输入说明: -一个正整数M (M< 10000)。
输出说明:输出合数的数量。
输入样例: 12
输出样例: 6
'''
# m=int(input('输入样例：'))
# s=0
# for i in range(1,m+1):
#     if (i%2==0 or i%3==0 or i%5==0 or i%7==0)and i not in (2,3,5,7):
#         s+=1
# print('输出样例：'+str(s))

'''
对于整数区间[N, M],已知0输入说明:两个整数N和M。
输出说明:顺序输出元素数位上各个数字的平方和大于元素本身的数。
输入样例: 21 25
输出样例: 25
'''
# nums=input('输入样例：')
# num1=int(nums.split()[0])
# num2=int(nums.split()[1])
# for i in range(num1,num2+1):
#     s=0
#     for j in str(i):
#         s+=int(j)**2
#     if s>i:
#         print('输出样例：'+str(i))

'''
判断输入的字符串中是否含有日期信息，满足条件的日期信息是指:年份在1979到2019之间，月份表
达为01到12，且年份信息和月份信息之间用’- '连接, 如”2010-06”就是满足条件的日期信息。如果
找到这样的日期信息,请输出该信息在字符串中的位置，即年份信息的第一个字符在字符串中出现的位
置,如果有多个满足条件的日期信息，仅输出第一个。如果字符串中不包含有效日期信息，请输出-1。说
明，输入字符串的第-个元素的位置是1。
'''
# a=input('输入样例：')
# year=a[a.find('-')-4:a.find('-')]
# month=a[a.find('-')+1:a.find('-')+3]
# if year=='' or month =='':
#     print('输出样例：-1')
# elif int(year) in range(1979,2019+1) and month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
#     print('输出样例：'+str(int(a.find(year))+1))
# else:
#     print('输出样例：-1')

'''
有一个DNA序列，用字符串S表示(仅包含’A'、' C'、' G’、' T’四种字符,长度
< 100000)。现有N个待检测的基因片段(序号分别是1.2...N)，字符串Ti (i=1,2...N) 示(仅包
含’A’、'C、'G’、'T’四种字符,长度<1000)。请分别检测DNA序列S中是否存在这些基因片
段，并按下面输出说明格式依次输出检测结果。
输入说明:第一行是DNA序列S。
第二行是正整数N,表明有N个待检测的基因片段，之后有N行,分别表示这N个待检测的基因片段,即每
行一个基因片段。
输出说明:依次匹配这N个待检测的基因片段，如果DNA序列S中存在第i个待检测的基因片段，输出Ti:
ALERT所在位置(即Ti的首字母在S中的位置,如果出现多次，输出第一次出现的位置，S的起始位置为
1) ;如果不存在则输出Ti: SAFE。
输入样例: ATCGCGCGAATTGATCGTTCGA
2
AATTGAT
GATCGTC
输出样例: T1: ALERT 9
T2: SAFE
'''
# s=input('输入样例：')
# s=s[:100000]
# line=input()
# li=[]
#
# for i in range(int(line)):
#     string=input()
#     string=string[:1000]
#     f=s.find(string)
#     if f!='':
#         li.append(int(f)+1)
#     else:
#         li.append(0)
#
# print('输出样例：',end='')
# for i in range(len(li)):
#     if li[i]!=0:
#         print('T'+str(i+1)+': ALTER',li[i])
#     else:
#         print('T'+str(i+1)+': SAFE')

'''
某冶金厂生产两类合金产品，分别为M1和M2。生产M1和M2时需要三种原材料(含某种原材料的需
求量为0的情形)。现有一 批这样的原材料即将过期，希望尽快用这些原材料生产M1和M2 (每种原材料
的数量均小于10000)，请给出浪费原材料总量最少(即三种剩余原材料的数量和最小)的生产方案。如
果方案不止一种，请输出M1生产量最少时所对应的方案。
输入说明:第- -行给出生产M1所需的三种原材料数量 ，为整型数据;
第二行给出生产M2所需的三种原材料数量,为整型数据;
第三行给出三种原材料的库存数,为整型数据。
输出说明:输出满足条件时，M1、M2各自的生产数量(整数解)。
输入样例: 4 2 2
6 3 2
20 10 10
输出样例: 2 2
'''

# t11, t12, t13 = map(int, input().split(' '))
# t21, t22, t23 = map(int, input().split(' '))
# t1, t2, t3 = map(int, input().split(' '))
# re1,re2,re3 = t1, t2, t3
# m1_max = min(t1 // t11, t2 // t12, t3 // t13)
# m1_c, m2_c, surplus = 10000, 10000, 10000
# for i in range(1, m1_max):
#     t1 = t1 - i * t11
#     t2 = t2 - i * t12
#     t3 = t3 - i * t13
#     m2_max = min(t1 // t21, t2 // t22, t3 // t23)
#     if m2_max <= 0:
#         num = t1 + t2 + t3
#         if num < surplus:
#             m1_c = i
#             m2_c = m2_max
#             surplus = num
#         break
#     else:
#         t1 = t1 - m2_max * t21
#         t2 = t2 - m2_max * t22
#         t3 = t3 - m2_max * t23
#         num = t1 + t2 + t3
#         if num < surplus:
#             m1_c = i
#             m2_c = m2_max
#             surplus = num
#     t1, t2, t3 = re1,re2,re3
# print(m1_c, m2_c)

'''
输入一串字符，由字母、数字和空格组成，长度<1000，判断其中是否存在日期格式的数据。日期格式的数据具有如下的特征，连续包含年份和月份信息。年份信息是指连续的四个数字，之后是Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec这些字符串之一,如”2019Nov”就是符合日期格式要求的数据。
输入说明:  输入一个字符串。
输出说明:  输出包含满足日期格式的字符子串；如果不包含，则输出2000Jan。
输入样例1:  Todayis2019Nov15th.
输出样例1： 2019Nov
输入样例2:  Todayisasunnyday.
输出样例2： 2000Jan
输入样例3:  OnNov05，nothing happen.
输出样例3： 2000Jan
'''
