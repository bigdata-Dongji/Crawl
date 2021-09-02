# encoding:utf8
'''
Creation time: 2020/12/5 11:50
Update time:
Purpose:
'''
from datetime import datetime
from elasticsearch_dsl import DocType,Date,Nested,Boolean,\
    analyzer,InnerObjectWrapper,Completion,Keyword,Text,Integer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=['localhost'])

class BlogType(DocType):
    # 技术博文类型
    title=Text(analyzer='ik_max_word')
    blog_url = Keyword()
    author = Text(analyzer='ik_max_word')
    publisher = Text(analyzer='ik_max_word')
    blog_type = Keyword()
    release_time = Text()
    tags = Text(analyzer='ik_max_word')
    likes = Integer()
    collection = Integer()
    reading = Integer()
    update_time = Text()
    content = Text(analyzer='ik_max_word')

    class Meta:
        index='hq_blog'
        doc_type='blog'


if __name__ == '__main__':
    BlogType.init()