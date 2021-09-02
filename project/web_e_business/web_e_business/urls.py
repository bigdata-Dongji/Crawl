"""web_e_business URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
import xadmin
from django.views.static import serve
# from goods.views_base import GoodsListView
from web_e_business.settings import MEDIA_ROOT
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
# 配置goods的url
router.register(r'goods',GoodsListViewSet,basename='goods')
# 配置goods的url
router.register(r'categorys',CategoryViewSet,basename='categorys')

# goods_list=GoodsListViewSet.as_view({
#        'get':'list',
# })

urlpatterns = [
       # path('admin/', admin.site.urls),
       url('^xadmin/', xadmin.site.urls),
       url('media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
       url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
       # 商品列表页
       # url(r'goods/$', goods_list,name='goods-list'),
       url(r'^',include(router.urls)),
       url(r'docs/$',include_docs_urls(title='湖汽电商'))
]
