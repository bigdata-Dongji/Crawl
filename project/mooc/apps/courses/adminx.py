# encoding:utf8
'''
Creation time: 2020/11/30 14:46 
Update time:
Purpose:
'''
import xadmin
from apps.courses.models import Course,Lesson,Video,CourseResource

class GlobalSettings(object):
    site_title='湖汽学习平台-后台管理系统'
    site_footer='大数据特长队'
    menu_style='accordion' # 菜单手风琴，可收缩

class BaseSettings(object):
    enable_themes=True  # 开启主题
    use_bootswatch=True

class CourseAdmin(object):
    list_display=['title','degree','learn_times','students']
    search_fields=['title','desc','detail','degree','students']
    list_filter=['title','teacher__name','desc','detail','degree','learn_times']
    list_editable=['degree','desc']

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course__title','name','add_time']
    # 加2个下划线__的意思是：在外键的title这个字段上进行过滤

class VideoAdmin(object):
    list_display=['lesson','name','add_time']
    search_fields=['lesson','name']
    list_filter=['lesson','name','add_time']

class CourseResourceAdmin(object):
    list_display=['course','name','file','add_time']
    search_fields=['course','name','file']
    list_filter=['course','name','file','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView,GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView,BaseSettings)