# encoding:utf8
'''
Creation time: 2020/12/4 15:02 
Update time:
Purpose:
'''
import sys
import os
from scrapy.cmdline import execute
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy','crawl','it_blog'])
execute(['scrapy','crawl','zhihu'])