#coding=utf-8
from lxml import etree
import time
from selenium import webdriver


def scroll_foot(self, browser):
    '''
    控制屏幕向下滚动一下
    :param driver:
    :return:
    '''
    js = "var q=document.documentElement.scrollTop=100000"
    return browser.execute_script(js)

def getTbodyList():
    return browser.find_elements_by_xpath('//div[@class="group-memeber"]//tbody[contains(@class,"list")]')

def parse():
    info=browser.find_elements_by_xpath('//*[@class="td-card"]')
    print(info)

def main():

    # 找到QQ群的人数
    qqNum = int(browser.find_element_by_xpath('//*[@id="groupMemberNum"]').text.strip())
    curren_qq_num = 0

    while curren_qq_num != qqNum:
        # 不停的向下滚动屏幕，直到底部，一边抽取数据

        scroll_foot(browser)
        time.sleep(1)
        # tlist = getTbodyList(browser)
        parse()
        # prelen = len(tlist)#更新tbody列表的长度

if __name__ == '__main__':
    qqgroup='484627756'
    url="https://qun.qq.com/member.html#gid=" + str(qqgroup)
    browser=webdriver.Chrome()
    browser.get(url)
    time.sleep(10)
    main()
