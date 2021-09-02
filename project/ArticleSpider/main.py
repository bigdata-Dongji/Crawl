from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy','crawl','news']) # 执行新闻采集
execute(['scrapy','crawl','xinpi']) # 执行披露信息采集
