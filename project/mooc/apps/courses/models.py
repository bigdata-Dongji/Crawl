# encoding:utf8
from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher,CourseOrg

class Course(models.Model):
    teacher=models.ForeignKey(Teacher,verbose_name='讲师',on_delete=models.CASCADE)
    course_org=models.ForeignKey(CourseOrg,null=True,blank=True,on_delete=models.CASCADE,verbose_name='课程机构')
    title=models.CharField(verbose_name='课程名',max_length=50)
    desc=models.CharField(verbose_name='课程描述',max_length=300)
    learn_times=models.IntegerField(default=0,verbose_name='学习时长（分钟）')
    degree=models.CharField(verbose_name='难度',choices=(('low','初级'),('normal','中级'),('high','高级')),max_length=6)
    students=models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums=models.IntegerField(default=0,verbose_name='收藏人数')
    click_nums=models.IntegerField(default=0,verbose_name='点击数')
    category=models.CharField(default=u'后端开发',max_length=20,verbose_name='课程类别')
    tag=models.CharField(default='',verbose_name='课程标签',max_length=10)
    youneed_know=models.CharField(default='',max_length=300,verbose_name='课程须知')
    teacher_tell=models.CharField(default='',max_length=300,verbose_name='老师告诉你')
    is_classics=models.BooleanField(default=False,verbose_name='是否经典课程')
    detail=models.TextField(verbose_name='课程详情')
    image=models.ImageField(upload_to='course/%Y/%m',verbose_name='封面图',max_length=100)


    class Meta:
        verbose_name='课程信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title

class Lesson(BaseModel):
    course=models.ForeignKey(Course,on_delete=models.CASCADE) # on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name=models.CharField(verbose_name='章节名',max_length=50)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长（分钟）')

    class Meta:
        verbose_name='课程章节'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.course

class Video(BaseModel):
    lesson=models.ForeignKey(Lesson,verbose_name='章节',on_delete=models.CASCADE)
    name = models.CharField(verbose_name='视频名称', max_length=50)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长（分钟）')
    url=models.CharField(max_length=200,verbose_name='访问地址')

    class Meta():
        verbose_name='视频'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class CourseResource(BaseModel):
    course = models.ForeignKey(Course, verbose_name='课程', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='资源名称', max_length=50)
    file=models.FileField(upload_to='course/resource/%Y/%m',verbose_name='下载地址',max_length=200)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name='课程资源'
        verbose_name_plural=verbose_name