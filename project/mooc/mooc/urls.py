"""mooc URL Configuration

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
from django.conf.urls import url,re_path
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from apps.users.views import LoginView,LogoutView
from apps.organizations.views import OrgView
from mooc.settings import MEDIA_ROOT
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hq/xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    # path('login/', TemplateView.as_view(template_name='login.html'),name='login'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('captcha/', include('captcha.urls')),

    # 配置上传文件的访问url
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    # 机构相关页面
    url(r'^org_list',OrgView.as_view(),name='org_list')
]
