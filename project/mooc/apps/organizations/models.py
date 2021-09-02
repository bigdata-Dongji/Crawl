from django.db import models

from apps.users.models import BaseModel

class City(BaseModel):
    name = models.CharField(max_length=30, verbose_name='城市')
    desc = models.CharField(max_length=200,verbose_name='描述')

    class Meta:
        verbose_name='城市'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class CourseOrg(BaseModel):
    name=models.CharField(max_length=50,verbose_name='机构名称')
    desc=models.TextField(verbose_name='描述')
    tag=models.CharField(default='全国知名',max_length=10,verbose_name='机构标签')
    category=models.CharField(default='college',verbose_name='机构类别',max_length=10,
                              choices=(('personal','个人'),('college','高校'),('training','培训机构')))
    click_nums=models.IntegerField(default=0,verbose_name='点击数')
    fav_nums=models.IntegerField(default=0,verbose_name='收藏数')
    image=models.ImageField(upload_to='org/%Y/%m',verbose_name='logo',max_length=100)
    address=models.CharField(max_length=150,verbose_name='地址')
    students=models.IntegerField(default=0,verbose_name='学习人数')
    course_nums=models.IntegerField(default=0,verbose_name='课程数')

    is_auth=models.BooleanField(default=False,verbose_name='是否认证')
    is_gold=models.BooleanField(default=False,verbose_name='是否金牌')

    city=models.ForeignKey(City,verbose_name='所在城市',on_delete=models.CASCADE)

    def courses(self):

        courses=self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name='合作机构'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Teacher(BaseModel):
    org=models.ForeignKey(CourseOrg,verbose_name='所属机构',on_delete=models.CASCADE)
    name=models.CharField(verbose_name='讲师名字',max_length=50)
    work_years=models.IntegerField(default=0,verbose_name='工作年限')
    work_company=models.CharField(max_length=50,verbose_name='工作单位')
    title=models.CharField(max_length=50,verbose_name='工作职称')
    points=models.CharField(max_length=50,verbose_name='教学特点')
    click_nums=models.IntegerField(default=0,verbose_name='点击数')
    fav_nums=models.IntegerField(default=0,verbose_name='收藏数')
    age=models.IntegerField(verbose_name='年龄')
    image = models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像', max_length=100)

    class Meta:
        verbose_name='讲师'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name