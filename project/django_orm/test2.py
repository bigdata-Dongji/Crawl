import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django.db.models import Count,Avg,Max,Min,Sum,F,Q
from courses.models import *


# 查看原生的SQL语句 query属性
res1=Course.objects.all().query
# 大小写不敏感查询，return: <QuerySet [<Teacher: Allen>, <Teacher: Jack>]>
res2=Teacher.objects.filter(nickname__icontains='a')

"""返回新QuerySet API"""
# 1.all()，filter(), order_ by(), exclude(), reverse(), distinct()
# exclude()排除
res3=Student.objects.exclude(nickname='A同学').values('nickname','age')
# reverse()反向排序
res4=Student.objects.exclude(nickname='A同学').values('nickname','age').reverse()
# distinct()去重

# 2.extra()，defer(), only() 实现字段别名，排除一些字段，选择一些字段
# extra()取别名，参数select={'别名':'字段名'}
res5=Student.objects.all().extra(select={'name':'nickname'}).values('nickname')
res6=Student.objects.all().extra(select={'name':'nickname'}).values('name')
# only()选择一些字段
res7=Student.objects.only('age').query

# 3.values(),values_ list() 获取字典或元组形式的QuerySet
res8=Student.objects.values('nickname','age')
res9=Student.objects.values_list('nickname','age')
# values_ list() 只有1个字段可以使用flat=True变成列表
res10=Student.objects.values_list('nickname',flat=True)

# 4.dates{)，datetimes() 根据 日期 或 时间日期 获取查询集
res11=Course.objects.dates('online','month',order='DESC')
res12=Course.objects.datetimes('created_at','hour',order='DESC')

# 5.union()，intersection()， difference() 并集、交集、差集     都会去重
res13=Course.objects.filter(price__gte=290).values('price')
res14=Course.objects.filter(price__gte=292).values('price')
res15=res13.union(res14)

# 6.select_ related() - 对一、多对-查询优化，prefetch_ related() 一对多、 多对多查询优化; _set()反向查询
res16=Course.objects.all().select_related('teacher')
res17=Student.objects.prefetch_related('course')
res18=Teacher.objects.get(nickname='Jack').course_set.all()

# 7.annotate()使用聚合计数、求和、平均数raw()执行原生的SQL
res19=Course.objects.values('teacher').annotate(co=Count('teacher'))
res20=Course.objects.values('teacher').annotate(co=Avg('price'))
res21=Course.objects.raw('select*from courses_course limit 2')
# for i in res21:
#     print(i.price)

# 5.其它操作exists(), count(), aggregate() 判断是否存在，统计个数，聚合
# annotate是分组后聚合  aggregate()是对表所有数据聚合
res22=Course.objects.aggregate(Max('price'),Min('price'))
# print(res22)

# F对象所有价格-10
# Course.objects.update(price=F('price')-10)
# F对象对2个相同类型字段进行比较
res23=Course.objects.filter(volume__lt=F('price')*10)
# print(res23)

# Q对象实现or语法，Q对象还可以实现not取反
res24=Course.objects.filter(Q(title__icontains='java')|Q(title__icontains='python'))
# and 语法
res25=Course.objects.filter(title__icontains='java',type=0)

# **可以将字典作为查询条件
res26=Course.objects.filter(**{'title__icontains':'java','type':0})

