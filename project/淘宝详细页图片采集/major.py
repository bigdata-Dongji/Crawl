import os
import re
from lxml import etree

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def search_product(keyword,frequency):
    i_frame=browser.find_element(By.ID,'q')
    i_frame.clear()
    time.sleep(1)
    i_frame.send_keys(keyword) # 输入关键字
    time.sleep(1)
    # from selenium.webdriver.common.keys import Keys
    # i_frame.send_keys(Keys.ENTER) # 按回车键
    if frequency!=1:
        button='submit'
    else:
        button='btn-search'
    browser.find_element(By.CLASS_NAME,button).click() # 找class名的按钮并点击
    time.sleep(10)
    shopname=input(str('请输入店铺名：'))  # 根据店铺名,再通过商品标题点击
    bt2=browser.find_element(By.XPATH,'//span[text()="{}"]/../../../..'.format(shopname))
    bt2.click()

    # with open('a.txt','w',encoding='utf8')as f:
    #     f.write(html)


def get_images(): # 获得图片链接
    n = browser.window_handles  # 获取当前页句柄
    # print(n)
    browser.switch_to.window (n[1]) # 切换到新的网页窗口
    time.sleep(1)
    html = browser.page_source # 获取网页源代码
    html = etree.HTML(html)
    browser.close()  # 源代码获取到了，可以关闭这个商品页面了
    browser.switch_to.window(n[0])
    previews=html.xpath('//*[@id="J_UlThumb"]/li/a/img/@src')
    # print(previews)
    classes=html.xpath('//ul[@class="tm-clear J_TSaleProp tb-img     "]/li/a/@style') # 分类图片，需要再匹配下
    # print(classes)
    details=html.xpath('//img[@class="img-ks-lazyload"]/@src')
    # print(details)
    for i in range(len(previews)):
        previews[i]=re.findall('//img.alicdn.com/.*?png|//img.alicdn.com/.*?jpg',previews[i])
    previews=[a for b in previews for a in b] # 因为re匹配结果是二维，我们用列表推导式将二维转一维方便后续处理
    for i in range(len(classes)):
        classes[i]=re.findall('//img.alicdn.com/.*?png|//img.alicdn.com/.*?jpg',classes[i])
    classes=[a for b in classes for a in b]
    return previews,classes,details

def save_image(item,prefix,brand,keyword): # 保存图片，参数1链接列表，参数2为文件命名前缀
    if item==[]:
        return
    path='D:\\图片素材\\淘宝\\宝贝分商品\\{}\\{}\\'.format(brand,keyword)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    if not os.path.exists(path):
        os.mkdir(path)
    print(item)
    for i in range(len(item)):
        try:
            if 'http' in item[i]:
                item[i] = re.findall('http.*?png|http.*?gif|http.*?jpg', item[i]) # 正则匹配结果是列表，所以下一步需要转一维
                item[i] =item[i][0] # 转一维
            else:
                item[i] = 'https:' + item[i]
                item[i] = re.findall('http.*?png|http.*?gif|http.*?jpg', item[i])  # 正则匹配结果是列表，所以下一步需要转一维
                item[i] = item[i][0]  # 转一维
            # if 'https:' not in item[i]:
            #     item[i]='https:'+item[i]
            suffix=item[i][-3:] # 文件后缀，可能是jpg，png，gif
            response = requests.get(item[i],headers=headers)
            file_path = path + prefix + '{}.{}'.format(str(i + 1),suffix)
            if not os.path.exists(file_path):
                with open(file_path,'wb')as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
        except requests.ConnectionError:
            print('Failed to save image')

def main():
    frequency=int(input('请输入执行次数：')) # 次数
    for i in range(1,frequency+1):
        keyword = input(str('关键字：'))
        start = time.time()
        search_product(keyword,i)
        img=get_images()
        brand = input(str('输入存放品牌文件夹：'))  # 分商品存放的品牌文件夹
        save_image(img[0],'preview',brand,keyword)
        time.sleep(1)
        save_image(img[1],'cla',brand,keyword)
        time.sleep(1)
        save_image(img[2],'d',brand,keyword)
        end=time.time()
        print('第',i,'次花费时间：',end-start)


if __name__ == '__main__':

    browser=webdriver.Chrome()
    browser.get('https://www.taobao.com')
    main()