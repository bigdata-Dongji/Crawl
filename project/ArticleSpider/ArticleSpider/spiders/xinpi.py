# -*- coding: utf-8 -*-
# 采集来源：中国资本市场信息披露平台

from urllib import parse
import scrapy
from scrapy import Request
from ArticleSpider.items import XinpiItem
import time
import random


class NewsSpider(scrapy.Spider):
    name = 'xinpi'
    allowed_domains = ['xinpi.cs.com.cn']
    start_urls = ['http://xinpi.cs.com.cn/page/xp/index.html']

    # def __init__(self, **kwargs):
        # self.browser = webdriver.Chrome()
        # url='http://xinpi.cs.com.cn/page/xp/index.html'
        # self.browser.get(url)
        # self.browser.find_element(By.ID,'nL4').click() # 点击栏目上市公司
    def handle_spider_closed(self, spider, reason):
        self.crawler.stats.set_value("failed_urls", ",".join(self.fail_urls))

    def parse(self, response):
        codes = 700000 # 结束代码
        for code in range(600000,codes):
            survey_url = 'http://zzw.hsmdb.com/iwin_zzbweb-webapp/info/v2/query/f10_company_profile?' \
                         'en_prod_code={}.SS'.format(str(code))  # 公司概况url
            pro_url = 'http://zzw.hsmdb.com/iwin_zzbweb-webapp/info/v2/query/f10_income_statement?' \
                      'en_prod_code={}.SS&page_no=1&page_count=1&order=time_desc'.format(str(code))  # 利润url
            xinpi_item = XinpiItem()
            index = code - 600000 + 1
            xinpi_item['index'] = index # 生成id索引
            yield Request(url=parse.urljoin(response.url,survey_url),callback=self.parse_survey,
                          meta={ "pro_url": pro_url,"xinpi_item": xinpi_item,"code": code},dont_filter=True)
            # 控制速度
            tr = random.uniform(0.7, 1.6)
            time.sleep(tr)

            print('采集完成第 ',index, ' 条数据')


    def parse_survey(self,response):
        pro_url = response.meta.get("pro_url", "")
        xinpi_item = response.meta.get("xinpi_item", "")
        code = response.meta.get("code", "")
        if response.text:

            dic1=dict(eval(response.text))
            try:
                mat1=dic1.get('data')[0].get('20101002')[0].get('{}.SS'.format(code))[0]
            except:
                print(111)
            chi_name=mat1.get('chi_name') # 公司名称
            email=mat1.get('email')
            indurstry=mat1.get('indurstry') # 所属行业
            reg_addr=mat1.get('reg_addr') # 注册地址
            legal_repr=mat1.get('legal_repr') # 法人代表
            general_manager=mat1.get('general_manager') # 总 经 理

            xinpi_item['chi_name']=chi_name
            xinpi_item['email']=email
            xinpi_item['indurstry']=indurstry
            xinpi_item['reg_addr']=reg_addr
            xinpi_item['legal_repr']=legal_repr
            xinpi_item['general_manager']=general_manager
            # print(chi_name, indurstry, general_manager, reg_addr, legal_repr, general_manager)

            tr = random.uniform(0.5, 2)
            time.sleep(tr)
            yield Request(url=parse.urljoin(response.url, pro_url),
                          meta={"xinpi_item": xinpi_item,"code": code},
                          callback=self.parse_pro, dont_filter=True)


    def parse_pro(self,response):

        xinpi_item=response.meta.get("xinpi_item", "")
        code = response.meta.get("code", "")
        if response.text:

            dic2 = dict(eval(response.text))
            try:
                mat2 = dic2.get('data')[0].get('20101019')[0].get('{}.SS'.format(code))[0]
            except:
                print(222)
            report_date = mat2.get('report_date')  # 报告日期
            operating_revenue = mat2.get('operating_revenue')  # 营业收入
            np_parent_company_owners = mat2.get('np_parent_company_owners')  # 归属母公司利润

            xinpi_item['report_date']=report_date
            xinpi_item['operating_revenue']=operating_revenue
            xinpi_item['np_parent_company_owners']=np_parent_company_owners
            # print(report_date,operating_revenue, np_parent_company_owners)
            yield xinpi_item


    # def start_requests(self):
        # from selenium.webdriver.chrome.options import Options
        #
        # chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        # browser = self.browser
        # browser.close()
        # n = browser.window_handles  # 获取当前页句柄
        # browser.switch_to.window(n[0])  # 切换到新的网页窗口
        # # 发现后面是个动态加载的html
        # html = browser.page_source
        # html = etree.HTML(html)
        # tds = html.xpath('//table[@id="table_CompanyList_012001"]/tbody/tr/td/a')
        # code=html.xpath('//table[@id="table_CompanyList_012001"]/tbody/tr/td/text()') # 拿到一页代号
        # for i in range(len(code)):
        #     code[i]=code[i].replace(' ','')
        #     code[i]=code[i].replace('"','')
        #     code[i]=code[i].replace('[','')
        #     code[i]=code[i].replace(']','')
        # print(code)
        # browser.find_element(By.XPATH,'//a[text()=2]').click()
        # time.sleep(2)

        # code = html.xpath('//table[@id="table_CompanyList_012001"]/tbody/tr/td/text()')  # 拿到一页代号
        # for i in range(len(code)):
        #     code[i] = code[i].replace(' ', '')
        #     code[i] = code[i].replace('"', '')
        #     code[i] = code[i].replace('[', '')
        #     code[i] = code[i].replace(']', '')
        # print(code)
        # with open('a.html','w',encoding='utf8')as f:
        #     f.write(browser.page_source)
        # print(n)
        # for i in range(len(tds)):
        #     tr = random.uniform(0.4, 2.1)
        #     time.sleep(tr)
        #     # 注意下面elements不能少s
        #     browser.find_elements(By.XPATH,'//table[@id="table_CompanyList_012001"]/tbody/tr/td/a')[i].click()
        #
        #
        #     n = browser.window_handles
        #     browser.switch_to.window(n[1])

        #     tr = random.uniform(0.4, 1.4)
        #     time.sleep(tr)
        #     # 这里加密了，需要进一步提取
        #     html = etree.HTML(browser.page_source)
        #     url=html.xpath( '//*[@id="content"]/iframe/@src')[0]
        #     browser.get(url)
        #     browser.find_element(By.XPATH,'//a[@id="gsjj"]').click()
        #     n = browser.window_handles
        #     browser.switch_to.window(n[2])
        #     url = html.xpath('//*[@id="content"]/iframe/@src')[0]
        #     browser.get(url)
        #     html = browser.page_source
        #     html = etree.HTML(html)
        #     name = html.xpath('//td[text()="公司名称"]/following-sibling::td/text()')  # 公司名称
        #     industry = html.xpath('//td[text()="所属行业"]/following-sibling::td/text()')  # 所属行业
        #     email = html.xpath('//td[text()="电子邮箱"]/following-sibling::td/text()')  # 电子邮箱
        #     addr = html.xpath('//td[text()="注册地址"]/following-sibling::td/text()')  # 注册地址
        #     boss = html.xpath('//td[text()="法人代表"]/following-sibling::td/text()')  # 法人代表
        #     manager = html.xpath('//td[text()="总 经 理"]/following-sibling::td/text()')  # 总 经 理
        #     website = html.xpath('//td[text()="公司网站"]/following-sibling::td/text()')  # 公司网站
        #     print(name, industry, email, addr, boss, manager, website)
        #     browser.close()
        #
        #     tr = random.uniform(0.4, 1.5)
        #     time.sleep(tr)
        #     browser.switch_to.window(n[1])
        #     browser.find_element(By.ID, 'lrb').click()
        #     browser.close()
        #     browser.switch_to.window(n[2])
        #     html = browser.page_source
        #     html = etree.HTML(html)
        #     date = html.xpath('//td[text()="申报日期"]/following-sibling::td/text()')  # 申报日期
        #     income = html.xpath('//td[text()="营业收入"]/following-sibling::td/text()')  # 营业收入
        #     profit = html.xpath('//td[text()="其中：归属母公司利润"]/following-sibling::td/text()')  # 收入归属母公司利润
        #     print(date, income, profit)
        #     browser.close()







