import requests
from lxml import etree
from bs4 import BeautifulSoup
from urllib.parse import urlparse,urljoin
from urllib.parse import parse_qs
import re
import sys
import random
import time

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        response=requests.get(url,headers=headers)
        response.encoding=response.apparent_encoding  # 转换编码
        # time.sleep(random.uniform(0.4, 1.7))
        if response.status_code==200:
            return response.text
    except requests.RequestException:
        return None

def parse_one_page(html):
#     pass
    html = BeautifulSoup(html, 'html.parser')
    title = html.select('#thread_subject')[0].string  # 帖子标题

    url = html.link['href']  # 帖子链接
    # content=html.find(attrs={'class':'t_fsz'}) # 发帖内容
    tid=re.findall('thread-(\d+)-',url)[0] # 链接里的tid,代表发帖
    author = html.select('.authi')[0].a.string  # 发帖用户名

    content_list = []  # 存储每一条评论,包括tid,内容和时间    tid就是pid
    for i in range(len(html.select('.pcb'))):
        tid = re.findall('authicon(\d+)"', str(html.select('.authicn')[i]))[0]
        if html.select('.pcb')[i].div['class'] == ['locked']:
            content = html.select('.pcb')[i].div.em.string

        elif i == 0:
            content = html.select('.t_f')[0].contents
            if len(content) > 1:
                content.remove(html.select('.t_f')[0].contents[1])
        else:
            content = re.sub('<a.*?>','',str(html.select('.pcb')[i].div.table.td))
        if html.select('#authorposton' + tid)[0].string != None:
            time = html.select('#authorposton' + tid)[0].string.replace('发表于 ', '')
        else:
            time = html.select('#authorposton' + tid)[0].span['title']
        content_list.append({'tid': tid, 'content': content, 'time': time})

    post_content = content_list[0]['content']  # 发帖内容
    user_list = []  # 存储每条评论的用户名和uid
    for i in range(len(html.select('.authi'))):
        if i % 2 == 0:
            user_name = html.select('.authi')[i].a.string
            uid = parse_qs(html.select('.authi')[i].a['href'])['uid'][0]
            user_list.append({'user_name': user_name, 'uid': uid})
    if html.select('.ts')[0].font==None:
        post_type=''
    else:
        post_type=html.select('.ts')[0].font.string # 帖子类型
    if html.select('.pg')==[]:
        page=1
    else:
        page=re.findall('\d+',html.select('.pg')[0].label.span.string)[0]  # 评论页数

    for i in range(len(user_list)):
        content=str(content_list[i]['content']).replace('<br/>','').replace('\\n','').replace("''",'').replace('\n','').replace('</blockquote>','')
        f.write('{},{},{},{},{},{},{},{}\n'.format(tid,title,post_type,user_list[i]['user_name'],
                user_list[i]['uid'],content_list[i]['time'],content_list[i]['tid'],content))
    return int(page)

def main(offset):

    url='https://www.discuz.net/forum-2-{}.html'.format(str(offset))
    html=get_one_page(url)
    html = BeautifulSoup(html, 'html.parser')
    link = html.select('.xst')
    for i in range(len(link)):
        print('正在爬取第{}页'.format((offset - 1) * 40 + i+1))
        url=urljoin('https://www.discuz.net/', link[i]['href'])
        html=get_one_page(url)
        page=parse_one_page(html)
        if page>1:
            for i in range(2,page+1):
                tmp = re.findall('\d{5}\d+-.*?-\d+', url)[0]
                tmp2 = tmp.replace('-1-', '-'+str(i)+'-')
                next_url = url.replace(tmp, tmp2)
                html=get_one_page(next_url)
                parse_one_page(html)

if __name__ == '__main__':
    f=open('data.csv','w',encoding='utf8')
    f.write('帖子ID,标题,类型,评论用户,UID,评论时间,TID,评论内容' + '\n')
    for i in range(1,500+1):
        main(i)
    f.close()





# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
#         }
# html=requests.get('https://www.discuz.net/thread-3849981-1-14.html',headers=headers)
# html=BeautifulSoup(html.text,'html.parser')






