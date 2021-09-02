import json
import random
# a=random.uniform(0.4,2.1) # 生成0.4-2.1之间的随机小数
# print(a)
# from lxml import etree
# import codecs
# f=codecs.open("a.html","r","utf-8")
# content=f.read()
# f.close()
# tree=etree.HTML(content)
# b_xpath='//table[@id="table_CompanyList_012001"]/tbody/tr/td/a'
# r=tree.xpath(b_xpath)
#
# # for i in range(len(r)):
# a=tree.xpath( '//*[@id="content"]/iframe/@src')[0]
# print(a)

from selenium import webdriver


from selenium.webdriver.chrome.options import Options

# server = Server(r'D:\Develop\browsermob-proxy-master\browsermob-dist\src\main\scripts\browsermob-proxy.bat')
# server.start()
# proxy = server.create_proxy()
#
# chrome_options = Options()
# chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
#
# base_url = "https://www.iesdouyin.com/share/user/63174596206"
# proxy.new_har("douyin", options={'captureHeaders': True, 'captureContent': True})
# driver.get(base_url)
#
# result = proxy.har
#
# for entry in result['logs']['entries']:
#     _url = entry['request']['url']
#     # 根据URL找到数据接口
#     if "/api/v2/aweme/post" in _url:
#         _response = entry['response']
#         _content = _response['content']['text']
#         # 获取接口返回内容
#         print(_content)
#
# server.stop()
# driver.quit()

with open('a.html','r',encoding='utf8')as f:
    a=f.read()

dic1=dict(eval(a))
mat1=dic1.get('data')[0].get('20101002')[0].get('600000.SS')[0]
chi_name=mat1.get('chi_name') # 公司名称
email=mat1.get('email')
indurstry=mat1.get('indurstry') # 所属行业
# reg_addr=mat1.get('reg_addr') # 注册地址
# legal_repr=mat1.get('legal_repr') # 法人代表
# general_manager=mat1.get('general_manager') # 总 经 理
print(chi_name,email)

dic2=dict(eval(a))
print(dic2)

try:
    mat2=dic2.get('data')[0].get('20101019')[0].get('600000.SS')[0]
except:
    print()
print('--')

# report_date=mat2.get('report_date') # 报告日期
# operating_revenue=mat2.get('operating_revenue') # 营业收入
# np_parent_company_owners=mat2.get('np_parent_company_owners') # 归属母公司利润

# print(chi_name,indurstry,general_manager,reg_addr,legal_repr,general_manager)
# print(operating_revenue,np_parent_company_owners)