import requests
import re
from lxml import etree
import time
import random
import json
#获取网页数据的方法
def get_url(url):
    #设置请求头模拟浏览器
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400",
        "cookie": "CCC_SE=ADC_t%2fbwMgAgVIPdbyanHfZDZGRlhADusJihrSUmlA5lhLgimTVinrTdH25tkCFCCC21hchshoxZIqN1t2Ab2UMjV1lfTBxvz6VB8mJO9SQXc5sn6fKwQ9lh4v3XddwITEaUtH2ASdA2ki0gjTYXizljQe6NBduRG%2bSwvtYnhGctev8NMJNSLtBiHCJKhENinDtBYVPNi%2bo2MwtpX6IrhJyZlMKeZvtf%2b17vlfMiFXw8m8DaALEMKMe2CVxxMmjyqMtziv0MFujs2awo4pdphSJvRMfw3RboX8nqcdZJVN%2fLp0oEPF94h%2fIK2TOBr7umRTvItjjWS45k0MSdWBp1OAgzrIvz742ZHQYkoiyvVYsUcp9hr7xjXZKpv0%2fmuCvCJ2YJuUkLlnYd%2bEa7RStjw8cEa%2fXDkdcT%2b3fYUaVy1Ro36LMjy6ke155i1njEa9MJ67xpLgOMxGJWyQDEEWXqL50dOO9qSDE2OHxaxtAKP3QvidonJU304WTZHQMkPS8lBToG5ocKj8rd1y6mlHNSsA6djQ%3d%3d; unpl=V2_ZzNtbUsDQkJ8CBFdfRtUDGJTGl8RVhBAcAsWVisQVQAzBBRUclRCFnQUR1xnGl4UZwIZXkpcQxFFCEdkeR1ZAmYBEV1yZ3MWdThHZHseXQRuABtdRlNFFHMATlN%2fHlgEYAYibUVXSiVFQxMIFV8dR1cDElpGUkEddwFHZHopXgRmABtdS1VDHUVDKFU2GVsEZgoRVEJTRxN0Dk5cfB1bAWYEF21CVkIUdAhCUXMebAY%3d; __jdc=122270672; __jdv=122270672|kong|t_35460321_|tuiguang|8e0f81f873984a93b0bd42a3a884e678|1600828157131; areaId=18; ipLoc-djd=18-1488-29447-0; __jdu=1600828155707996565064; shshshfp=9d6e4a4581113378fa4fb5077770f68e; shshshfpa=4358eccc-aeea-f20e-4b35-d3e6fc2e5adf-1600828158; shshshfpb=qzp1rRGdIC%2FNBtYLi22VNNg%3D%3D; 3AB9D23F7A4B3C9B=CIP4VYADVEOSPLX5HIIX2RTC3M2BEG744PUG2HM5RGCA5LY3JYUSS2J7BNMRPOCWMRFSNJANHZEIIY5WLZBRAERLFU; wlfstk_smdl=5niznyelm6ywg2z4kurvodxwpj5fim1n; __jda=122270672.1600828155707996565064.1600828155.1600846146.1600849698.4; __jdb=122270672.2.1600828155707996565064|4.1600849698; shshshsID=f00c377196a25cbdba0f7b23dee6a106_2_1600849743090"
    }

    response = requests.get(url, headers=head)  # timeout=5
    if response.status_code == 200:
        # response.encoding = 'utf-8'
        html = response.text
        return html
    else:
        return None

#获取子页面的方法
def get_urls(html):
    urls1 = []
    s = etree.HTML(html)
    link = s.xpath('//*[@id="J_goodsList"]/ul/li[*]/@data-sku')
    for i in link:
        urls = 'https:' + '//item.jd.com/' + i + '.html'
        urls1.append(urls)
    return urls1


#获取数据的方法
def Productinformation(urls,id,id3):
    #打开以一个文件
    file = open('./京东笔记本电脑信息.txt', "a", encoding="utf-8")

    # 获取json网页数据 价格
    jg = []
    id3 = id3.replace('jQuery2765786([', '').replace(']);', '')
    id4=re.findall('"p":"(.*?)",',str(id3))
    try:
        #将获取的价格添加进jg变量中
        jg.append(str(id4[0]))
    except:
        pass

    # 获取 json网页数据 销量，好评，中评，差评
    xiaoliang=[]
    hp=[]
    zp=[]
    cp=[]
    id = id.replace('jQuery3473299(','').replace(');','')
    json_data = json.loads(id)
    for j in json_data['CommentsCount']:
        #异常处理 获取数据时 报错跳过
        try:
            xiaoliang.append(j['CommentCount'])
            hp.append(j['GoodCount'])
            zp.append(j['GeneralCount'])
            cp.append(j['PoorCount'])
        except:
            pass

    print('数据爬取中---------------------------------------------------------------------------------------------------------------------------------------------------')
    #过8秒爬取一个页面 作用：防止被封ip
    time.sleep(8)

    #获取数据 获取数据的方式是 正则表达式
    # （.*?） 想要的数据
    name=re.findall("<li title=.*?>品牌： <a href=.*? clstag=.*? target='_blank'>(.*?)</a>",urls)
    numbering = re.findall("<li title=.*?>商品编号：(.*?)</li>", urls)
    product_name = re.findall("<li title=.*?>商品名称：(.*?)</li>", urls)
    graphic = re.findall("<li title=.*?>显卡类别：(.*?)</li>", urls)
    thickness = re.findall("<li title=.*?>厚度：(.*?)</li>", urls)
    Types_of = re.findall("<li title=.*?>类型：(.*?)</li>", urls)
    ram = re.findall("<li title=.*?>内存容量：(.*?)</li>", urls)
    solid = re.findall("<li title=.*?>固态硬盘（SSD）：(.*?)</li>", urls)
    # 数据组装  把所有获取的字段 全部存入data
    data = name + numbering + product_name + jg + graphic  + thickness  + Types_of  + ram + solid + xiaoliang + hp + zp + cp
    if int(len(data)) != 13:
        pass

    else:
        # 存入数据到txt
        file.write(str(data))
        file.write('\n')
        print(data)


#2获取详情页面
def main(url):
    poe=0
    #拼接连接
    for i in get_urls(get_url(url)):
        print(i.strip('https://item.jd.com/.html'))
        Productinformation(get_url(i), get_url("https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + i.strip('https://item.jd.com/.html') + "&callback=jQuery3473299&_=1600841705794"),get_url("https://p.3.cn/prices/mgets?callback=jQuery2765786&type=1&area=18_1488_29447_0&pdtk=&pduid=1600828155707996565064&pdpin=&pin=null&pdbp=0&skuIds=J_"+i.strip('https://item.jd.com/.html')+"%2CJ_10021632660677%2CJ_10021457773546%2CJ_72484394767%2CJ_10020453171189%2CJ_10021299636805%2CJ_10021252793702%2CJ_10021095802963%2CJ_5155905%2CJ_6772447%2CJ_10021182120327&ext=11100000&source=item-pc"))
        # Productinformation(get_url(i), get_url("https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + i.strip('https://item.jd.com/.html') + "&callback=jQuery3473299&_=1600841705794"),get_url("https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=" + i.strip('https://item.jd.com/.html') +"&score=" + str(poe) +"&sortType=5&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1"),get_url("https://p.3.cn/prices/mgets?callback=jQuery2765786&type=1&area=18_1488_29447_0&pdtk=&pduid=1600828155707996565064&pdpin=&pin=null&pdbp=0&skuIds=J_"+i.strip('https://item.jd.com/.html')+"%2CJ_10021632660677%2CJ_10021457773546%2CJ_72484394767%2CJ_10020453171189%2CJ_10021299636805%2CJ_10021252793702%2CJ_10021095802963%2CJ_5155905%2CJ_6772447%2CJ_10021182120327&ext=11100000&source=item-pc"))

#1获取主网页
if __name__ == '__main__':
    #翻页
    for t in range(1, 200, 2):
        url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&suggest=1.def.0.0&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&page=" + str(t)
        main(url)


