from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

UserProfile=get_user_model()

class UserAsk(BaseModel):
    name=models.CharField(max_length=30,verbose_name='姓名')
    mobile=models.CharField(max_length=11,verbose_name='手机号')
    org_name=models.CharField(max_length=50,verbose_name='机构名称')

    class Meta:
        verbose_name='合作咨询'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{}_{}({})'.format(self.org_name,self.name,self.mobile)

class CourseComment(BaseModel):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='课程')
    comment=models.CharField(max_length=200,verbose_name='评论')

    class Meta:
        verbose_name='课程评论'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.user

class Userfavorite(BaseModel):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='用户')
    fav_id=models.IntegerField(verbose_name='数据id')
    fav_type=models.IntegerField(choices=((1,'课程'),(2,'机构'),(3,'讲师')),default=1,verbose_name='收藏类型')

    class Meta:
        verbose_name='用户收藏'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{}_{}'.format(self.name.username,self.fav_id)

class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE, verbose_name='用户')
    message = models.CharField(max_length=200, verbose_name='消息内容')
    has_read=models.BooleanField(default=False,verbose_name='是否已读')

    class Meta:
        verbose_name='用户消息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.message

class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,verbose_name='用户')
    course = models.ForeignKey(Course,on_delete=models.CASCADE, verbose_name='课程')


    class Meta:
        verbose_name='用户课程'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.course.name