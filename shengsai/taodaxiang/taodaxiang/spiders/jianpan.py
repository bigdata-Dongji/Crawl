# -*- coding: utf-8 -*-
import scrapy
import hashlib
import time


class JianpanSpider(scrapy.Spider):
    name = 'jianpan'
    allowed_domains = ['taodaxiang.com']
    start_urls = ['https://taodaxiang.com/rank/index/get']


    def start_requests(self):
        times = time.time()
        cookies = {"Cookie":"addo=ture; PHPSESSID=pbcjcvfr0e9spn0htfchbf5a86; endpage=10; Hm_lvt_5a903fe4f343bef5b71db5664648022b=1608362318,1608897295,1608900028; VnbGm_auth=a0ccUlYFUVVWU1FWBgQBDQQGVVQJU1YBDF9XUgBXCVJVZFwoMXQNLCAhIDRjYlQIc3ZQJ3Q0Xm12b1FVeHROcHlwcRIwYDAsIiIWU0R1RHJmdQYwaTRzXFF4B3twY29wcXNmKDd0UDM0NQZed3VfcmB0djBgIGRIRm9BeGNxTkZXZ2ZWJHIgMz4iGwl1dl9xZHMGNGQiY1ty; jiathis_rdcdh=e337dbca2b7e542d73e4272075662eba; jiathis_rdcdhcc=96f0a190986ed55124c246fd4c7e412f; Hm_lpvt_5a903fe4f343bef5b71db5664648022b=1608900131; VnbGm_sp=5656CAMBBgZTBggAAFdTAFUHAFUHUApRUV1QDg8HVQNbYWl1cWdaYDdjX2JkZwYoVndxeGM3cyxjJAB0bzcOL3pzCVxpdWdjL2VtYlZwBiBXYUACejZjI3E3RkJvIDRSbHNueXhwB38tZQhDc3AgL2JiW15lJ2RTdCYAdF4zNDt%2FYn5xcGZORjpnaUN0chksbHdbbGg3cAl8NkYGfyAFBW5heVd0ZGBkNGNpYmVnKTNgYGIHYDleFWEmAXBiJhUNWWR%2Bcn9jc3QGZ35%2BeHIkLFdlW3BrJ1UvdjNWUmIjJDhrc19iZXBwbDF0aQVRcDAeYXJAe3cgAzd0JGcPbyBTM3Vmbgl0ZncPOXN%2BYmlkCix4dgd7YSACFX8hVgZuNw8je3tuTAFjcAIyYXl%2BamMkBXxrT1JQOXQrYSYBcGIgBSN7cF9xfHNBDip3X1RmcAYwcWtfdGsldApwMmB4dCRSOGFgCWlgcmR3LXdpV3N0MA12cUBdfiMDM3EkXXRwNSAnd2FUT2t0cAYmYQh1ZXIKK31mUGd5JlUNdiZjXWgqFS9oYnoIcmdgdCFhbVRqZCBfdWV2fHAzZF93IFZdaSYzJ3R2UH15c1FvBXVQXGVyFjR9ZXF0aideAWMhAFl7MzRXXWJuUFZpdGwCc19%2BfHIwDXp1ZndjJXA%2FfycATnAhCiRhc3luVmB3ezJ1eXF9dBYnZWRyZ3klRS9nMV0DcDUkGmp0UH14enACBnNpBWNnMF91ZGYHVjkCX1Y9AVVpOwksXGRQfXdnUQYhdX1HaWUG"}
        head = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'addo=ture; PHPSESSID=pbcjcvfr0e9spn0htfchbf5a86; endpage=10; Hm_lvt_5a903fe4f343bef5b71db5664648022b=1608362318,1608897295,1608900028; VnbGm_auth=a0ccUlYFUVVWU1FWBgQBDQQGVVQJU1YBDF9XUgBXCVJVZFwoMXQNLCAhIDRjYlQIc3ZQJ3Q0Xm12b1FVeHROcHlwcRIwYDAsIiIWU0R1RHJmdQYwaTRzXFF4B3twY29wcXNmKDd0UDM0NQZed3VfcmB0djBgIGRIRm9BeGNxTkZXZ2ZWJHIgMz4iGwl1dl9xZHMGNGQiY1ty; jiathis_rdcdh=e337dbca2b7e542d73e4272075662eba; jiathis_rdcdhcc=96f0a190986ed55124c246fd4c7e412f; Hm_lpvt_5a903fe4f343bef5b71db5664648022b=1608900131; VnbGm_sp=2227U1RUAQcJA1NVBFdWBw4AU1NVBwNTXlMCBwRSVFpTIGUqIiZ3fW1wJShwIlwwciJkK2t2EgJuJ1JRZmU1JycgcjU8IF15WmAINHgiRzR3MnRQV3MJIGAjJVlTZTUSICJyIi8md35yYDYWeiJXFm8ldFxlcTQWeiIUf2hiMho3IHU5MidjVHBhDxJzIEgraSdZI1FhJzNzNDIAYGYyETMgdRAnJQB5bnBSKHEicyt6MXdUZHQzUmwlU29rcCIFBDMFISI2SW5zYlIoYCBlOHc2YyBwZjMsbyc1Y2RmJScjIkM5MiYAbW5xFFBiIkcrYDVjNHt2Eid6JDIEY3EUVwckZQg2J1Z%2Bc3UUK1A2Wyt1JgU0YnZVN3QnIgB1cTQvJgRiEx0iXVxocg80fiZyI242XgFQdFQ%2FbCVTb2tyMismJ2UiJSZ3W19yMgZ2IkckbzRnJHBgEg1pIg9zdmFTJzU5WDI3IFl2cnIUAnomRwJ7NmNRenUSI3skBH9wZCYWPyNTCyU1XXVsayE8ZiBbLGg2Uih6cAI%2FeSQbRWtgIiM1I3YUISYAU3tyGyR%2BIXYGazRjL3RyCRZ6IwQBYHAELyklZi4sJmd1cHAxDnUgVyBZNgQkfWY0DnoxIlJhdjUJLzdyCwEzSW1ddiIrcSBHAncyBAZncyAvcScUAHBwCBE1OXImLiFWAnh3UgZ%2BJkcgYDRwKHpzElZsNyUFY3dSWzc5XCIrAV1cXGBSDnciZgZrNXNUUnQgFls%2BU3RgaTYkATNmLioyZ0NucFMdeTdH',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',

        }
        data = {'media': 3,
                'pattern': 0,
                'sort': 0,
                'q': '机械键盘',
                'wwid': '*',
                'goodid': '',
                'area_id': 0,
                'curpage': 1,
                'startpage': 1,
                'endpage': 10,
                "filters":{"type":"all"},
                'rtime': str(hashlib.md5(str(times).encode()).hexdigest())}
        yield scrapy.FormRequest(
            url=self.start_urls[0],
            cookies=cookies,
            formdata=data,
            callback=self.parse,
            headers=head
        )

    def parse(self, response):
        time.sleep(60)
        print(response.text)
        # pass


from scrapy.cmdline import execute
execute(['scrapy','crawl','jianpan'])
