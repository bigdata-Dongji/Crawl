# encoding:utf8
'''
Creation time: 2020/12/3 18:41 
Update time:
Purpose:
'''
import xadmin
from.models import UserFav,UserLeavingMessage,UserAddress
class UserFavAdmin():
    list_display=['user','goods','add_time']
    search_fields=['goods']
    list_filter=['user','goods','add_time']

class UserLeavingMessageAdmin():
    list_display=['user','msg_type','message','subjects','file','add_time']
    search_fields = ['message','subjects']
    list_filter=['user','msg_type','message','subjects','file','add_time']

class UserAddressAdmin():
    list_display = ['user', 'district', 'address','singer_name','singer_mobile','add_time']
    search_fields = ['user', 'district', 'address','singer_name','singer_mobile']
    list_filter = ['user', 'district', 'address','singer_name','singer_mobile','add_time']

xadmin.site.register(UserFav,UserFavAdmin)
xadmin.site.register(UserLeavingMessage,UserLeavingMessageAdmin)
xadmin.site.register(UserAddress,UserAddressAdmin)