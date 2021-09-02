# encoding:utf8
import requests,random,time,os,re
from lxml import etree
def req(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.encoding=response.apparent_encoding
        time.sleep(random.uniform(0.5,1.2))
        return response.text
    except:
        ...
def parse(text):
    try:
        html=etree.HTML(text)
        title=html.xpath('//div[@class="newsshow_title"]/text()')[0].strip()
        content=html.xpath('//div[@class="newsshow_wnnr"]/descendant-or-self::*/text()')
        string=''
        for i in content:
            character_map = {
                # ord('\n'): ' ',
                ord('\t'): ' ',
                ord('\r'): None,
            }
            i=i.replace('xa01','')
            i=i.replace('xa02','')
            i=i.replace('xa03','')
            i=i.translate(character_map)
            string+=i
        if not os.path.exists('data'):
            os.mkdir('data')
        path_ = re.sub('[ ? * : " < > \ / | ]', '', title)
        path = 'data/' + path_ + '.txt'
        with open(path, 'w', encoding='utf8')as file:
            file.write(title)
            file.write('\n')
            file.write(str(string))
            file.write('\n')
    except:
        ...



def main():
    types=['行业新闻','企业动态','常见问题']
    end=[12,3,6]
    for i in range(1,4):
        print(f'开始爬取 {types[i-1]} 类数据中。。。')
        for j in range(1,end[i-1]+1):
            print(f'正在爬取第{j}页')
            url = f'http://www.tegujx.com/news-{i}-{j}.html'
            text = req(url)
            html=etree.HTML(text)
            urls=html.xpath('//div[@class="news_nr"]/ul/li/a/@href')
            urls=['http://www.tegujx.com/'+h for h in urls]
            for url_ in urls:
                text=req(url_)
                parse(text)

    print('爬取完成！！！')



if __name__ == '__main__':
    main()
