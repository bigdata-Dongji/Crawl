import requests
from lxml import etree
import random
import time,pymysql

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        response=requests.get(url,headers=headers)

        time.sleep(random.uniform(0.5, 1.8))  # 请求1次休息0.5-1.8秒
        if response.status_code==200:
            return response.text
    except requests.RequestException:
        return None

def parse_one_page(html):
#     pass
#
# with open('test.txt',encoding='utf8')as f:
#     html=f.read()

    html=etree.HTML(html)
    title=html.xpath('//div[@id="wrapper"]/h1/span/text()')[0] # 书名
    author=html.xpath('//div[@id="info"]/span/a/text()')  # 作者
    author2=html.xpath('//div[@id="info"]/span[text()="作者:"]/following-sibling::a/text()')  # 作者
    if author!=[]:
        author = author[0]
    elif author2!=[]:
        author = author2[0].strip()
    else:
        author=''

    infoname=html.xpath('//div[@id="info"]/span/text()')
    info=html.xpath('//div[@id="info"]/text()')

    for i in range(len(infoname)):
        infoname[i]=infoname[i].split()
    while [':']in infoname:
        infoname.remove([':'])
    while [] in infoname:
        infoname.remove([])
    while ['作者:'] in infoname:
        infoname.remove(['作者:'])
    while ['/'] in infoname:
        infoname.remove(['/'])
    string = [''] * 15  # 定义保存csv的字符串的空变量
    while ['丛书:'] in infoname:
        infoname.remove(['丛书:'])
        # 丛书
        series=html.xpath('//div[@id="info"]/span[text()="丛书:"]/following-sibling::a/text()')
        if series:
            string[10] = series[0]
    while ['出品方:'] in infoname:
        infoname.remove(['出品方:'])
        # 出品方
        producer=html.xpath('//div[@id="info"]/span[text()="出品方:"]/following-sibling::a/text()')
        if producer:
            string[3] = producer[0]
    while ['译者:'] in infoname:
        infoname.remove(['译者:'])
    for i in range(len(info)):
        info[i]=info[i].split()
    while [] in info:
        info.remove([])
    # infoname  [['出版社:'], ['出版年:'], ['页数:'], ['定价:'], ['装帧:'], ['ISBN:']]
    # info  [['南海出版公司'], ['2013-1-1'], ['538'], ['39.50元'], ['精装'], ['9787544258609']]
    # series 丛书
    # producer  ['新经典文化', '新经典文库·东野圭吾作品'] 第1个出品方，第2个丛书


    string[0]=title
    string[1]=author

    # print(infoname)
    # print(info)


    for i in [['出版社:'], ['副标题:'], ['原作名:'], ['出版年:'], ['页数:'], ['定价:'], ['装帧:'], ['ISBN:']]:
        if ['出版社:'] in infoname:
            string[2] =info[infoname.index(['出版社:'])][0]
        if ['副标题:'] in infoname:
            string[4] = info[infoname.index(['副标题:'])][0]
        if ['原作名:'] in infoname:
            string[5] = info[infoname.index(['原作名:'])][0]
        if ['出版年:'] in infoname:
            string[6] = info[infoname.index(['出版年:'])][0]
        if ['页数:'] in infoname:
            string[7] = info[infoname.index(['页数:'])][0]
        if ['定价:'] in infoname:
            string[8] = info[infoname.index(['定价:'])][0]
        if ['装帧:'] in infoname:
            string[9] = info[infoname.index(['装帧:'])][0]
        if ['ISBN:'] in infoname:
            string[11] = info[infoname.index(['ISBN:'])][0]

    score=html.xpath('//strong[@class="ll rating_num "]/text()')[0]
    string[12]=score.strip()
    scorenum=html.xpath('//span[@property="v:votes"]/text()') # 评价数
    if scorenum:
        scorenum=scorenum[0]
    else:
        scorenum=0
    string[13]=scorenum
    labels=html.xpath('//div[@id="db-tags-section"]/div/span/a/text()')
    string[14]=labels


    out=''
    for i in string:
        out+=str(i)+','
    out=out[:-1]+'\n'
    # print(string)

    # print(out) # 变成可写入csv的字符串

    # with open('doubun22.csv','a',encoding='utf8')as f:
    #     f.write(out)

    sql='insert into douban_novel values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'\
        .format(string[0],string[1],string[2],string[3],string[4],string[5],string[6],string[7],string[8],string[9],string[10],string[11],string[12],string[13],string[14])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print(sql)
        db.rollback()


def main(offset):


    url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'.format(offset) # 爬取 小说 标签书籍
    html=get_one_page(url)
    html = etree.HTML(html)
    childurls = html.xpath('//li[@class="subject-item"]/div/h2/a/@href')

    for childurl in childurls:
        html=get_one_page(childurl)
        parse_one_page(html)



columns = '书名,作者,出版社,出品方,副标题,原作名,出版年,页数,定价,装帧,丛书,ISBN,豆瓣评分,评价数,常用标签\n'
if __name__ == '__main__':
    db = pymysql.connect('localhost', 'root', 'root', 'bookdb')  # 创建MySQL连接对象
    cursor = db.cursor()  # 创建游标

    # with open('doubun.csv','w',encoding='utf8')as f:
    #     f.write(columns)
    for i in range(200):
        print('爬取完成了{}条'.format(i*20))
        main(offset=i*20)


