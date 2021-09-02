# encoding:utf8
'''
Creation time: 2020/12/3 19:45 
Update time:
Purpose:
'''
import xadmin
from .models import GoodsCategory, GoodsCategoryBrand, Goods,GoodsImage,Banner


class GlobalSettings(object):
    site_title='湖汽电商平台-后台管理系统'
    site_footer='大数据特长队'
    # menu_style='accordion' # 菜单手风琴，可收缩

class BaseSettings(object):
    enable_themes=True  # 开启主题
    use_bootswatch=True

xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSettings)

class GoodsCategoryAdmin():
    list_display = ['name', 'code', 'desc', 'category_type','parent_category','is_tab','add_time']
    search_fields = ['name',  'desc', 'category_type','parent_category__name']
    list_filter = ['name', 'code', 'desc', 'category_type','parent_category','is_tab','add_time']


class GoodsCategoryBrandAdmin():
    list_display = ['name','desc','image','add_time']
    search_fields = ['name','desc']
    list_filter = ['name','desc','image','add_time']


class GoodsAdmin():
    list_display = ['goods_sn', 'name', 'click_num', 'sold_num','fav_num','goods_num','market_price','shop_price']
    search_fields = ['name','goods_brief','goods_desc']
    list_filter = ['goods_sn', 'name', 'click_num', 'sold_num','fav_num','goods_num','market_price','shop_price']

class GoodsImageAdmin():
    list_display = ['goods', 'image_url', 'image', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['goods', 'image_url', 'image', 'add_time']

class BannerAdmin():
    list_display = ['goods', 'index', 'image', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['goods', 'index', 'image', 'add_time']

xadmin.site.register(GoodsCategory,GoodsCategoryAdmin )
xadmin.site.register(GoodsCategoryBrand,GoodsCategoryBrandAdmin )
xadmin.site.register(Goods,GoodsAdmin )
xadmin.site.register(GoodsImage,GoodsImageAdmin )
xadmin.site.register(Banner, BannerAdmin)