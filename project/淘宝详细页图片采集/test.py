from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
#
#
# driver.get('https://www.baidu.com')
# i_frame=driver.find_element(By.ID,'kw')
# i_frame.send_keys('hhh')
# i_frame.clear()
# i_frame.send_keys('h2222h')
# js='window.open("https://www.sogou.com");'
# driver.execute_script(js)
# windows=driver.window_handles
# driver.switch_to.window(windows[1])
# driver.close()
# driver.back()
# time.sleep(1)
# driver.forward()
#
# import requests
# headers={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
#         }
# url='https://img.alicdn.com/imgextra/i4/920668840/O1CN01KESQqo2FAlovXNYKf_!!920668840.jpg_60x60q90.jpg'
# url=url.replace('60x60','800x800')
# response=requests.get(url,headers=headers)
# with open('a.jpg','wb')as f:
#     f.write(response.content)
import time

import requests
from lxml import etree
import os
# # html='<div><a><span class="1"><img src="222">hh</span><span id="2">hh2</span>0</a><a><span id="2">hh</span>1</a></div>'
# # html=etree.HTML(html)
# html=etree.parse('a.html',etree.HTMLParser())
# result=html.xpath('//*')
# #
# print(result)
import re
# t=['aaa//img.alicdn.com/imgextra/i4/920668840/O1CN01Hz6OcR2FAlp2F8Pnc_!!920668840.jpgbbb', 'ww//img.alicdn.com/imgextra/i4/920668840/O1CN01Hz6OcR2FAlp2F8Pnc_!!920668840.jpg']
# for i in range(len(t)):
#     t[i]=re.findall('//img.alicdn.com/.*?jpg',t[i])
# t=[a for b in t for a in b]
# print(t)
# start=time.time()
# with open('a.txt','r',encoding='utf8')as f:
#     a=f.read()
# html=etree.HTML(a)
# item=html.xpath('//div[@id="description"]/div/p/img/@src')
# # r=re.findall('//img.alicdn.com/.*?jpg',a)
# # for i in range(len(item)):
# #     item[i]=re.findall('//img.alicdn.com/.*?jpg',item[i])
# path='D:\\图片素材\\淘宝\\宝贝分商品\\摩豹\\{}\\'.format('摩豹N1')
# prefix='d'
#
# headers={
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
#         }
# print(item[1])
# for i in range(len(item)):
#     try:
#         if 'https:' not in item[i]:
#             item[i] = 'https:' + item[i]
#         response = requests.get(item[i])
    #     file_path = path + prefix + '{}.jpg'.format(str(i+1))
    #     if not os.path.exists(file_path):
    #         with open(file_path, 'wb')as f:
    #             f.write(response.content)
    #     else:
    #         print('Already Downloaded', file_path)
    # except requests.ConnectionError:
    #     print('Failed to save image')
# if 'https:' not in item[1]:
#     item[1] = 'https:' + item[1]
# time.sleep(1)
# end=time.time()
# print(end-start)
# response = requests.get(item[1],headers=headers)
# with open('j.jpg','wb')as f:
#     f.write(response.content)
# print(len(result))
# print(result)
# item='//img.alicdn.com/imgextra/i1/920668840/O1CN01jziuCY2FAlos5zdKv_!!920668840.jpg'
# if 'https:' not in item:
#     item = 'https:' + item
# print(item)
import numpy as np
# item=['https://img.alicdn.com/imgextra/i1/2878410103/O1CN01KHN1WS1CdDN5NzI7T_!!2878410103.png', 'https://img.alicdn.com/imgextra/i4/2878410103/O1CN01Q4zdqT1CdDN0qOUQT_!!2878410103.png', 'https://img.alicdn.com/imgextra/i1/2878410103/O1CN01My0Ajp1CdDN2FjI3k_!!2878410103.png', 'https://img.alicdn.com/imgextra/i3/2878410103/O1CN01mitsOr1CdDN6xguEZ_!!2878410103.png', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif', '//img.alicdn.com/tps/i4/T10B2IXb4cXXcHmcPq-85-85.gif']
# for i in range(len(item)):
#
#     if 'http' in item[i]:
#         item[i] = re.findall('http.*?jpg|http.*?png|http.*?gif', item[i])  # 正则匹配结果是列表，所以下一步需要转一维
#         print(item)
#         item[i] = item[i][0]  # 转一维
# item='aa.gif'

# print(item[-3:])
a='https://img.alicdn.com/imgextra/i4/2479377904/O1CN01oujrHW28G56V3dIM9_!!2479377904.png_40x40q90.jpg'
b=re.findall('http.*?png|http.*?jpg|http.*?gif',a)
print(b)