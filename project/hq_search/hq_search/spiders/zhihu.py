import scrapy
from selenium import webdriver
import time
import pickle
from mouse import move,click
from selenium.webdriver.chrome.options import Options
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response, **kwargs):
        ...

    def start_requests(self):
        chrome_option=Options()
        chrome_option.add_argument('--disable-extensions')
        chrome_option.add_experimental_option('debuggerAddress','127.0.0.1:9222')

        browser=webdriver.Chrome(chrome_options=chrome_option)
        try:
            browser.maximize_window() # 窗口最大化
        except:
            ...
        browser.get('https://www.zhihu.com/signin')
        browser.find_element_by_xpath('//div[@class="SignFlow-tabs"]/div[2]').click()
        username=browser.find_element_by_xpath('//input[@name="username"]')
        username.clear()
        username.send_keys('17708428636')
        passwd=browser.find_element_by_xpath('//input[@name="password"]')
        passwd.clear()
        passwd.send_keys('hhghsd') # 先输入错误的密码
        browser.find_element_by_xpath('//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]').click()
        time.sleep(6)
        login_success=False
        while login_success:
            try:
                notify_ele=browser.find_element_by_xpath('//*[@class="Tabs-link AppHeader-TabsLink is-active"]')
                login_success=True
            except:
                pass
            try:
                english_captcha_element=browser.find_element_by_class_name('Captcha-englishImg')
            except:
                english_captcha_element =None
            try:
                chinese_captcha_element=browser.find_element_by_class_name('Captcha-chineseImg')
            except:
                chinese_captcha_element =None

            if chinese_captcha_element:
                ele_position=chinese_captcha_element.location
                x_relative=ele_position['x']
                y_relative=ele_position['y']
                browser_navigation_panel_height=browser.execute_script(
                    'return window.outerHeight - window.innerHeight;')
                base64_text=chinese_captcha_element.get_attribute('src')
                import base64
                code=base64_text.replace('data:image/jpg;base64,','').replace('%0A','')
                fh=open('yzm_cn.jpeg','wb')
                fh.write(base64.b64decode(code))
                fh.close()

                from zheye import zheye
                z = zheye()
                positions = z.Recognize('yzm_cn.jpeg')
                last_position = []
                if len(positions) == 2:
                    if positions[0][1] > positions[1][1]:
                        last_position.append([positions[1][1], positions[1][0]])
                        last_position.append([positions[0][1], positions[0][0]])
                    else:
                        last_position.append([positions[0][1], positions[0][0]])
                        last_position.append([positions[1][1], positions[1][0]])
                    first_position=[int(last_position[0][0]/2),int(last_position[0][1]/2)]
                    second_position=[int(last_position[1][0]/2),int(last_position[1][1]/2)]
                    move(x_relative+first_position[0],y_relative+browser_navigation_panel_height+first_position[1])
                    click()
                    time.sleep(3)
                    move(x_relative+second_position[0],
                         y_relative+browser_navigation_panel_height+second_position[1])
                    click()
                else:
                    last_position.append([positions[0][1], positions[0][0]])
                    first_position = [int(last_position[0][0] / 2), int(last_position[0][1] / 2)]
                    move(x_relative + first_position[0],
                         y_relative + browser_navigation_panel_height + first_position[1])
                    click()
                username = browser.find_element_by_xpath('//input[@name="username"]')
                username.clear()
                username.send_keys('17708428636')
                passwd = browser.find_element_by_xpath('//input[@name="password"]')
                passwd.clear()
                passwd.send_keys('hhh12345')
                browser.find_element_by_xpath(
                    '//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]').click()


                # def start_requests(self):

            if english_captcha_element:
                base64_text = chinese_captcha_element.get_attribute('src')
                import base64
                code = base64_text.replace('data:image/jpg;base64,', '').replace('%0A', '')
                fh = open('yzm_en.jpeg', 'wb')
                fh.write(base64.b64decode(code))
                fh.close()
                from tools.yundama_requests import YDMHttp
                yundama=YDMHttp('')
        '''
        知乎登录2种解决方案：
        1、下载Chrome60 driver2.33
        2、手动启动chromedriver
        我们选择2：
            1、启动chrome（确保所有chrome都关闭）
            2、使用cmd的命令：chrome.exe --remote-debugging-port=9222
            3、可以访问localhost:9222/json有description描述
        '''
        # cookies=pickle.load(open('D:/engineering\\python_code\\aca\\t_2020\\case\\hq_search\\data\\zhihu.cookie','rb'))
        # cookie_dict = {}
        # for cookie in cookies:
        #     cookie_dict[cookie['name']]=cookie['value']
        #
        # return [scrapy.Request(url=self.start_urls[0],dont_filter=True,cookies=cookie_dict)]

        # chrome_option=Options()
        # chrome_option.add_argument('--disable-extensions')
        # chrome_option.add_experimental_option('debuggerAddress','127.0.0.1:9222')
        #
        # browser=webdriver.Chrome(chrome_options=chrome_option)
        # browser.get('https://www.zhihu.com/signin')

        # browser.find_element_by_xpath('//div[@class="SignFlow-tabs"]/div[2]').click()
        # browser.find_element_by_xpath('//input[@name="username"]').send_keys('17708428636')
        # browser.find_element_by_xpath('//input[@name="password"]').send_keys('') # 输入密码
        # browser.find_element_by_xpath('//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]').click()

        # cookies=browser.get_cookies()
        #
        # pickle.dump(cookies,open('','wb'))



