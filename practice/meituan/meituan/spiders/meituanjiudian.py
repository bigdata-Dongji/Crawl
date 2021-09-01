# -*- coding: utf-8 -*-
import scrapy
import json
from meituan.items import MeituanItem       #导入items的自定义方法调用

class MeituanjiudianSpider(scrapy.Spider):
    name = 'meituanjiudian'
    allowed_domains = ['hotel.meituan.com']         #获取美团酒店的影藏链接
    start_urls = ['http://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&cityId=59&offset=%s&limit=20&startDay=20191210&endDay=20191210'%i for i in range(0, 1001, 20)]

    def parse(self, response):
        html = json.loads(response.text)        #将数据进行json解析
        for i in html['data']['searchresult']:      #循环数据的键值对，方便取值
            item = MeituanItem()    #调用items的方法进行数据的规范化
            item['name'] = i['name']        #使用items的自定义字段获得准确数据
            item['addr'] = i['addr']
            item['commentsCountDesc'] = i['commentsCountDesc']
            item['scoreIntro'] = i['scoreIntro'].split(" ")[0]
            item['hotelStar'] = i['hotelStar']
            item['historySaleCount'] = i['historySaleCount']
            print(item)
            # yield item          #将数据进行返回，并且使用自带方法进行数据存储成csv



'''
https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=A6C52ED35ED3289FB64DA1C27CB02CE4DEB33EE89D24D06FC9F0A2FBDE8819E5%401575939741516&cityId=59&offset=0&limit=20&startDay=20191210&endDay=20191210&q=&sort=defaults&X-FOR-WITH=92bzNnRiJbSTvD4%2BR%2BymaCy9a7DNi2%2BO4q4U5PkdTRcWMnfXlZoqIeA64d%2BZlCAnTUAAY6xVDfk61cHv1E3XlC9TQHxOendgFyett7o46McvXWsyJDqIy3hXfOfSNlNkVJ3kIQ9JM1HU4%2BBiEdRX9UtDjIuxImMuryL%2F%2FOUDTq6D8BCBOwQApOeTIlK1sC%2Bnp6zJq%2BIIH1k%2BVynK8rsvsA%3D%3D
https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=A6C52ED35ED3289FB64DA1C27CB02CE4DEB33EE89D24D06FC9F0A2FBDE8819E5%401575939741516&cityId=59&offset=0&limit=20&startDay=20191210&endDay=20191210&q=&sort=defaults&X-FOR-WITH=92bzNnRiJbSTvD4%2BR%2BymaCy9a7DNi2%2BO4q4U5PkdTRcWMnfXlZoqIeA64d%2BZlCAnTUAAY6xVDfk61cHv1E3XlC9TQHxOendgFyett7o46McvXWsyJDqIy3hXfOfSNlNkVJ3kIQ9JM1HU4%2BBiEdRX9UtDjIuxImMuryL%2F%2FOUDTq6D8BCBOwQApOeTIlK1sC%2Bnp6zJq%2BIIH1k%2BVynK8rsvsA%3D%3D
https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=A6C52ED35ED3289FB64DA1C27CB02CE4DEB33EE89D24D06FC9F0A2FBDE8819E5%401575939884165&cityId=59&offset={}&limit=20&startDay=20191210&endDay=20191210&q=&sort=defaults&X-FOR-WITH=OhQVfCBmB5KTgSltTvvJXloulv%2FHrT5Tw6k%2Fhu4%2B5%2B1rg%2FoKMscCDvvQjTTI0zserP0s7xXwSLVATqSPxvUd3Lroc2%2FRZQD3i2w%2BwYWTLC47x7%2FmEPvakGGTl0OCve89PA0VeQGkVXnfIyovolcCVzdwrOl4yQRpWcoDEmkXpZbaeHEvb6j4VgslsGZ74PJYWQtkwCe1Ve6phqv42EVzTCnukx8YJ7Xd4Q0JqRcFgMs%3D
'''