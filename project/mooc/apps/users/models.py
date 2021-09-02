# encoding:utf8
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nickname=models.CharField(max_length=50,verbose_name='昵称',default='')
    birthday=models.DateField(verbose_name='生日',null=True,blank=True)
    gender=models.CharField(verbose_name='性别',choices=(('male','男'),('female','女')),max_length=6)
    address=models.CharField(max_length=100,verbose_name='地址',default='')
    mobile=models.CharField(max_length=11,verbose_name='手机号')
    image=models.ImageField(verbose_name='用户头像',upload_to='head_image/%Y/%m',default='default.jpg')

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        abstract=True  # abstract为True时就不会生成表