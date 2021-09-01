# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy框架.shengsai.Job51.Job51.items import Job51Item
import re
import json

class A51jobSpider(CrawlSpider):
    name = '51job'
    allowed_domains = ['jobs.51job.com | search.51job.com/']
    start_urls = [f'https://search.51job.com/list/040000,000000,0000,00,9,99,python%2520%25E7%2588%25AC%25E8%2599%25AB,2,{i}.html' for i in range(1,6)]

    def start_requests(self):
        for i in self.start_urls:
        # url = self.start_urls[0]
            cookies = {
                "Cookie":"guid=84d4f8f811d2b9fd83611c7f5610db1c; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; ps=needv%3D0; 51job=cuid%3D180630394%26%7C%26cusername%3Dphone_17378237053_202010218850%26%7C%26cpassword%3D%26%7C%26cname%3D%25C5%25ED%25CC%25CE%26%7C%26cemail%3D1977153072%2540qq.com%26%7C%26cemailstatus%3D0%26%7C%26cnickname%3D%26%7C%26ccry%3D.0MTNvBEl77vQ%26%7C%26cconfirmkey%3D19m8GLpUirJsE%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3D19KZNbp3UpCqs%26%7C%26to%3De79a493d86a62495a68ef10606d11a505f9643c1%26%7C%26; adv=adsnew%3D1%26%7C%26adsnum%3D2004282%26%7C%26adsresume%3D1%26%7C%26adsfrom%3Dhttps%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.a000000Iwwi4_GU5Sj5thgvK_4-ae4KkBPLb0Gi2eGX0bD4vN5ldGuLxtZdsg_hfwgusKv9KCu8nL6AvaoFQHoANat7E-QeJZOFwdzTJeRVmn9VFfugMoDJcWsdSP2PLC87wFPu45wQR54sjZBr0yCmL_m769pB9UdLOkbkMeKEBIhkDFok1WIZmDsnkQNTswp6JJGBVf6yxav8JNW39t3HoJZpI.DR_NR2Ar5Od66CHnsGtVdXNdlc2D1n2xx81IZ76Y_uQQr1F_zIyT8P9MqOOgujSOODlxdlPqKMWSxKSgqjlSzOFqtZOmzUlZlS5S8QqxZtVAOtIOtHOuS81wODSgL35SKsSXKMqOOgfESyOHjGLY51xVOeNH5exS88Zqq1ZgVm9udSnQr1__oodvgvnehUrPL72xZgjX1IIYJN9h9merzEuY60.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPH7JUvc0IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqPH7JUvc0ThPv5HD0IgF_gv-b5HDdnWc1rjb3njf0UgNxpyfqnHn3PjfdP1D0UNqGujYknjT4nWcdnsKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5R420APzm1Y1PjDvnf%2526ck%253D9309.5.64.796.150.991.402.205%2526dt%253D1607932229%2526wd%253D51job%2526tpl%253Dtpl_11534_23295_19442%2526l%253D1522389804%2526us%253DlinkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E3%25252580%25252590%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A751Job%252525E3%25252580%25252591-%25252520%252525E5%252525A5%252525BD%252525E5%252525B7%252525A5%252525E4%252525BD%2525259C%252525E5%252525B0%252525BD%252525E5%2525259C%252525A8%252525E5%25252589%2525258D%252525E7%252525A8%2525258B%252525E6%25252597%252525A0%252525E5%252525BF%252525A7%2521%252526linkType%25253D%26%7C%26ad_logid_url%3Dhttps%253A%252F%252Ftrace.51job.com%252Ftrace.php%253Fadsnum%253D4178503%2526ajp%253DaHR0cHM6Ly9ta3QuNTFqb2IuY29tL3RnL3NlbS9MUF8yMDIwXzEuaHRtbD9mcm9tPWJhaWR1YWQ%253D%2526k%253Dd946ba049bfb67b64f408966cbda3ee9%2526bd_vid%253D10812075398951479616%26%7C%26; partner=www_baidu_com; slife=lastlogindate%3D20201214%26%7C%26; search=jobarea%7E%60040000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60040000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython+%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch1%7E%60190200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython+%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch2%7E%60190200%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA03%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython+%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch3%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython+%C5%C0%B3%E6%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21recentSearch4%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21collapse_expansion%7E%601%7C%21"
            }
            yield scrapy.Request(
                url=i,
                cookies=cookies,
                callback=self.parse_item
            )



    def parse_item(self, response):
        # print(response.url)
        datas = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]  # 查看到需要的数据在一个长标签层，恰好是一个字典形式
        data = json.loads(datas)  # 将数据清洗一下，使用json.lodas将字符串转换为字典
        for i in data['engine_search_result']:  # 将字典进行遍历
            item = Job51Item()
            item['job_name'] = i['job_name']  # 职位
            item['job_href'] = i['job_href']  # 职位链接
            item['company_name'] = i['company_name']  # 公司名称
            item['company_href'] = i['company_href']  # 公司链接
            item['providesalary_text'] = i['providesalary_text']  # 工资
            item['workarea_text'] = i['workarea_text']  # 地址
            item['updatedate'] = i['updatedate']  # 更新时间
            item['companytype_text'] = i['companytype_text']  # 公司类型
            item['jobwelf'] = i['jobwelf']  # 福利待遇
            item['attribute_text'] = i['attribute_text']  # 学历要求
            print(item)
            yield (item)


from scrapy.cmdline import execute
execute(['scrapy','crawl','51job'])
# execute(['scrapy','crawl','51job','-o','51job.csv'])
# execute(['scrapy','crawl','51job','-o','ml51job.json','-s','FEED_EXPORT_ENCODING=utf-8'])


'''
https://search.51job.com/list/040000,000000,0000,00,9,99,python%2520%25E7%2588%25AC%25E8%2599%25AB,2,3.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
https://search.51job.com/list/040000,000000,0000,00,9,99,python%2520%25E7%2588%25AC%25E8%2599%25AB,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
https://search.51job.com/list/040000,000000,0000,00,9,99,python%2520%25E7%2588%25AC%25E8%2599%25AB,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
'''

