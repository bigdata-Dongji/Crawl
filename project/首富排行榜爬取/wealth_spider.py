import requests,pymysql
from lxml import etree
def req(url):
    headers={
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding=response.apparent_encoding
    return response.text
def parse(text):
    html=etree.HTML(text)
    rank=html.xpath('//td[@class="xh"]/text()')
    print(rank)
    name=html.xpath('//a[@class="cty"]/@title')
    print(name)
    wealth=[]
    sourse=[]
    region=[]
    for i in range(len(rank)):

        wealth_=html.xpath(f'//tbody/tr[{i+2}]/td[3]/text()')

        sourse_=html.xpath(f'//tbody/tr[{i+2}]/td[4]/text()')

        region_=html.xpath(f'//tbody/tr[{i+2}]/td[5]/a/text()')
        try:
            wealth.append(wealth_[0])
        except:
            wealth.append('未知')
        try:
            sourse.append(sourse_[0])
        except:
            sourse.append('未知')
        try:
            region.append(region_[0])
        except:
            region.append('未知')
    return rank,name,wealth,sourse,region
def store(rank,name,wealth,sourse,region):
    db = pymysql.connect('localhost', 'root', 'root', 'breach2020')
    cursor = db.cursor()
    for i in range(len(rank)):
        sql = f'insert into wealth values({rank[i]},"{name[i]}","{wealth[i]}","{sourse[i]}","{region[i]}")'
        try:
            cursor.execute(sql)
            db.commit()

        except:
            db.rollback()
            print('error')
    cursor.close()
    db.close()
def main(url):
    text=req(url)
    lists=parse(text)
    store(lists[0],lists[1],lists[2],lists[3],lists[4])

if __name__ == '__main__':
    url='https://www.phb123.com/renwu/fuhao/shishi_{}.html'
    for i in range(1,11):
        print(f'爬取第{i}页中。。。')
        main(url.format(i))