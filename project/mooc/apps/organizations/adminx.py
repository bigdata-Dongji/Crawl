# encoding:utf8
'''
Creation time: 2020/11/30 14:46 
Update time:
Purpose:
'''
import xadmin
from apps.organizations.models import Teacher,CourseOrg,City

class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company']
    search_fields = ['org','name','work_years','work_company']
    list_filter = ['org','name','work_years','work_company']

class CourseOrgAdmin(object):
    list_display = ['name','desc','click_nums','fav_nums']
    search_fields = ['name','desc','click_nums','fav_nums']
    list_filter = ['name','desc','click_nums','fav_nums']

class CityOrgAdmin(object):
    list_display=['id','name','desc'] # 默认显示
    search_fields=['name','desc'] # 搜索框
    list_filter=['name','desc','add_time']  # 过滤器
    list_editable=['name','desc'] # 编辑标签

xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(City,CityOrgAdmin)