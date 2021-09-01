# -*- coding: utf-8 -*-
import scrapy


class Login3cqcSpider(scrapy.Spider):
    name = 'login3cqc'
    allowed_domains = ['login3.scrape.center']
    start_urls = ['https://login3.scrape.center/page/1']

    def start_requests(self):
        data = {
            "password": "admin",
            'username': "admin"
        }
        cookies= {
            "Cookie":"UM_distinctid=1762cf1eb185ba-0164bac7bc3611-230346d-1fa400-1762cf1eb19422"
        }
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Authorization': 'jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjA4MDU2Nzg3LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsIm9yaWdfaWF0IjoxNjA4MDEzNTg3fQ.cJVvyFJA8B67J1ApUeKNW3IrSygbnvy2Qua2ewhimI4',
            'Connection': 'keep-alive',
            'Cookie': 'UM_distinctid=1762cf1eb185ba-0164bac7bc3611-230346d-1fa400-1762cf1eb19422',
            'Host': 'login3.scrape.center',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        }

        url = self.start_urls[0]
        yield scrapy.FormRequest(
            url=url,
            pase={"username": "admin", "password": "admin"},
            callback=self.parse,
            cookies=cookies,
            headers=headers
        )

    def parse(self, response):
        print(response.text)

from scrapy.cmdline import execute
execute(['scrapy','crawl','login3cqc'])
        # pass

