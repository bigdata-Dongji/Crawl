# encoding:utf8
'''
Creation time: 2020/12/3 19:24 
Update time:
Purpose:
'''
import xadmin
from.models import ShoppingCart,OrderInfo,OrderGoods
class ShoppingCartAdmin():
    list_display =['user','goods','goods_nums','add_time']
    search_fields=['goods']
    list_filter=['user','goods','goods_nums','add_time']

class OrderInfoAdmin():
    list_display =['user','order_sn','pay_status','order_mount','post_script','pay_time']
    search_fields =['user','singer_name','order_sn']
    list_filter =['user','order_sn','trade_no','pay_status','post_script','order_mount','pay_time','address','singer_name','singer_mobile','add_time']

class OrderGoodsAdmin():
    list_display=['order','goods','goods_num','add_time']
    search_fields=['goods']
    list_filter=['order','goods','goods_num','add_time']

xadmin.site.register(ShoppingCart,ShoppingCartAdmin)
xadmin.site.register(OrderInfo,OrderInfoAdmin)
xadmin.site.register(OrderGoods,)

