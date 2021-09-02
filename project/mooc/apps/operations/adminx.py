# encoding:utf8
'''
Creation time: 2020/11/30 15:54 
Update time:
Purpose:
'''
import xadmin
from apps.operations.models import UserAsk,CourseComment,UserCourse,Userfavorite,UserMessage

class UserAskAdmin(object):
    list_display = ['name','mobile','org_name','add_time']
    search_fields = ['name','mobile','org_name']
    list_filter = ['name','mobile','org_name','add_time']

class CourseCommentAdmin(object):
    list_display = ['user','course','comment','add_time']
    search_fields = ['user','course','comment']
    list_filter = ['user','course','comment','add_time']

class UserCourseAdmin(object):
    list_display = ['user','course','add_time']
    search_fields = ['user','course']
    list_filter = ['user','course','add_time']

class UserfavoriteAdmin(object):
    list_display = ['user','fav_id','fav_type','add_time']
    search_fields = ['user','fav_id','fav_type']
    list_filter = ['user','fav_id','fav_type','add_time']

class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read']
    list_filter = ['user','message','has_read','add_time']

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComment,CourseCommentAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(Userfavorite,UserfavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)