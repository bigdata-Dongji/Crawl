# encoding:utf8
'''
Creation time: 2020/12/4 19:46 
Update time:
Purpose:
'''
import hashlib

def get_md5(url):
    if isinstance(url,str):
        url=url.encode('utf8')
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    print(get_md5('https://coding.imooc.com/class/chapter/92.html#Anchor'))