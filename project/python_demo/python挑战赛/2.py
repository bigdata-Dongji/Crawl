# encoding:utf8
'''
Creation time: 2020/11/27 15:10 
Update time:
Purpose:
'''

'''
16.将整数数组中是6的倍数的元素按照输入次序依次输出。如果没有符合条件的元素则输出-1。
输入说明:第一行是整数N (N<10000) ，表示数组中的元素个数,第二行是这个数组中的N个元素，规
元素中至少包含一个满足条件的元素。
输出说明:输出数组序列中6的倍数,如果有两个以上满足条件的元素，中间用空格隔开。
输入样例: 6
2 3 6 12 28 45
输出样例: 6 12
'''
# n=int(input())
# num=input().split()
# is_have=0
# for i in range(n):
#     if int(num[i])%6==0:
#         is_have=1
#         print(num[i],end=' ')
# if is_have==0:
#     print(-1)

'''
"输入一串字符，由字母、数字和空格组成，长度<1000，判断其中是否存在日期格式的数据。
日期格式的数据具有如下的特征，连续包含年份和月份信息。年份信息是指连续的四个数字，
之后是Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec这些字符串之一,
如”2019Nov”就是符合日期格式要求的数据。
输入说明:  输入一个字符串。
输出说明:  输出包含满足日期格式的字符子串；如果不包含，则输出2000Jan。
输入样例1:  Todayis2019Nov15th.
输出样例1： 2019Nov
输入样例2:  Todayisasunnyday.
输出样例2： 2000Jan
输入样例3:  OnNov05，nothing happen.
输出样例3： 2000Jan"
'''
# import re
# s=input()
# res=re.findall('\d{4}',s)
# is_true=0
# for i in range(len(res)):
#     if s[int(s.find(res[i]))+4:int(s.find(res[i]))+7] in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
#         print(res[i]+s[int(s.find(res[i]))+4:int(s.find(res[i]))+7])
#         is_true=1
# if is_true==0:
#     print('2000Jan')
'''
平面上有N个矩形（编号依次为1，2，…, N），每个矩形可用它的左下角和右上角顶点坐标来表示（默认该矩形的4条边分别两两平行于X轴或Y轴，所以确认这2个顶点后，矩形是唯一的），现在给出一些矩形，规定它们的面积各不相同，请输出面积第三大的矩形序号及其面积。
输入说明：第一行输入一个整数N（3<=N<=1000），之后N行，每行有两个二维坐标(x,y)，分别表示对应矩形的左下角和右上角的顶点坐标。
输出说明：面积第三大的矩形序号和它的面积，中间用空格隔开。
输入样例：5
          0 0 1 2  
          0 0 1 2 
          0 0 3 5  
          1 2 5 6  
          4 3 8 8  
输出样例：3 15
'''
# n=int(input())
# li=[]
# for i in range(n):
#     m=input()
#     xy=list(map(int,m.split()))
#     x=xy[2]-xy[0]
#     y=xy[3]-xy[1]
#     li.append(x*y)
# li[li.index(max(li))]=0
# li[li.index(max(li))]=0
# print(li.index(max(li))+1,max(li))

'''
"某机械公司生产两种产品。A的单件利润分别是100元，B的单件利润是150元。
每种产品由三种材料构成，现给出每种材料的库存（库存小于100000），求利润最大的生产方案。
输入说明: 第一行给出生产每件A产品所需要的三种材料数量；
第二行给出生产每件B产品所需要的三种材料数量；
第三行给出三种材料的库存数量。
输出说明: 输出利润最大生产方案所对应的每种产品的生产数量（按照产品A、产品B的顺序）
和利润最大值，每个数值间用空格隔开。
输入样例:  3 1 2
          5 2 2
          30 4 6
输出样例：2 1 350

样例信息提示：每件产品A需要材料一3、材料二1、材料三2；每件产品B需要材料一5、材料二2、材料三2。目前库存材料一为30、材料二为4、材料三为6。
采用生产A产品2件、B产品1件的生产方案，利润为350，达到利润最大值。"
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
# print(m1_c, m2_c,m1_c*100+m2_c*150)
