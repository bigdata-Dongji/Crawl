# encoding:utf8
'''
Creation time: 2020/11/26 15:16 
Update time:
Purpose:
'''
from lxml import etree
with open('test.html',encoding='utf8') as f :
    html=f.read()

html=etree.HTML(html)
print(html.xpath('//*[@id="amore"]/@href'))
a=html.xpath('//div[@class="sons"]')
for i in a:
    if len(i.xpath('.//a/b/text()'))>0:
        print(''.join(i.xpath('.//div[@class="contson"]//text()')).strip())
# print(a)

