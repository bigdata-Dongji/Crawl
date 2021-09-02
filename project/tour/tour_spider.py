import requests,time
from lxml import etree

def req(url):
    headers={
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4315.4 Safari/537.36'
    }
    resonse=requests.get(url,headers=headers)
    time.sleep(1)
    return resonse.text

def parse(html):
    html=etree.HTML(html)
    li =html.xpath('.//div[@class="theinfo"]')
    for i in li:
        title=i.xpath('.//p[@class="title"]/span/@name')[0]
        price=i.xpath('.//div[@class="tnPrice"]//em/text()')[0]
        # 出游人数
        try:
            tourist=i.xpath('.//p[@class="person-num"]/i/text()')[0]
        except:
            tourist=0
        # 点评人数
        try:
            dianping=i.xpath('.//p[@class="person-comment"]/i/text()')[0]
        except:
            dianping =0
        # 满意度（百分比）
        percent=i.xpath('.//*[@class="comment-satNum"]/span/i/text()')[0]
        # 副标题（包括出发地点，成团地点等。。）
        subtitle=i.xpath('.//*[@class="subtitle"]//span/text()')
        subtitle=''.join(subtitle)
        print(title)
        s='{},{},{},{},{},{}\n'.format(title,price,tourist,dianping,percent,subtitle)
        print(s)
        with open('data.csv','a',encoding='utf8')as f:
            f.write(s)

if __name__ == '__main__':
    with open('data.csv','w+',encoding='utf8')as f:
        f.write('title,price,tourist,dianping,percent,subtitle\n')
    base_url='https://s.tuniu.com/search_complex/whole-zhz-0-%E6%B5%99%E6%B1%9F/list-d50241/'
    for page in range(1,100):
        url=base_url+str(page)
        text=req(url)
        parse(text)
