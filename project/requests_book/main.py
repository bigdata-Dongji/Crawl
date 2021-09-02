# coding=utf8
import requests,pymysql,json
from lxml import etree


def req(url):
    headers={
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding=response.apparent_encoding
    return response.text

def parse(text):
    json_data=json.loads(text).get('data')
    for i in json_data:
        id=i.get('PARENTTAGID')
        classes=i.get('PARENTTAGNAME')
        print('正在爬取的类别：',classes)
        url='https://www.ptpress.com.cn/hotBook/getHotBookList?parentTagId={}&rows=18&page=1'
        c_text=req(url.format(id))
        c_data=json.loads(c_text).get('data').get('rows')
        for j in c_data[:5]:
            name=j.get('bookName')
            bookid=j.get('bookId')
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
            }
            cc_url='https://www.ptpress.com.cn/bookinfo/getBookDetailsById'
            cc_text=requests.post(cc_url,data={'bookId':bookid},headers=headers).text
            cc_json=json.loads(cc_text).get('data')

            author=cc_json.get('author')
            price=cc_json.get('discountPrice')
            info=cc_json.get('authorIntro').get('data')

            print(name,'\t',author,'\t',price,'\t',info)
            with open('data.txt','w+',encoding='utf8')as f:
                f.write('{},{},{},{},{}'.format(classes,name,author,price,info))



if __name__ == '__main__':
    url='https://www.ptpress.com.cn/hotBook/getParentTagIdList'
    text=req(url)
    parse(text)