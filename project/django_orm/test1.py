import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()

from app01.models import *
from django.db.models import Max,Min,Avg,Q,Count,Sum

# 查找所有书名里包含金老板的书
res1=Book.objects.filter(title__contains='金老板').all()

# 查找出版日期是2018年的书
res2=Book.objects.filter(publish_date__year=2018)

# 查找出版日期是2017年的书名
res3=Book.objects.filter(publish_date__year=2017)

# 查找价格大于10元的书
res4=Book.objects.filter(price__gt=10)

# 查找价格大于10元的书名和价格
res5=Book.objects.filter(price__gt=10).values('title','price')

# 查找memo字段是空的书
res6=Book.objects.filter(memo__isnull=True)


# 查找在北京的出版社
res7=Publisher.objects.filter(city='北京')

# 查找名字以沙河开头的出版社
res8=Publisher.objects.filter(name__startswith='沙河')
#
# 查找“沙河出版社”出版的所有书籍
res9=Book.objects.filter(Publisher__name='沙河出版社')

# 查找每个出版社出版价格最高的书籍价格
res10=Publisher.objects.values('name').annotate(max=Max('book__price'))

# 查找每个出版社的名字以及出的书籍数量
res11=Publisher.objects.values('name').annotate(c=Count('book__title'))

#
# 查找作者名字里面带“小”字的作者
res12=Author.objects.filter(name__contains='小')

# 查找年龄大于30岁的作者
res13=Author.objects.filter(age__gt=30)

# 查找手机号是155开头的作者
res14=Author.objects.filter(phone__startswith=155)

# 查找手机号是155开头的作者的姓名和年龄
res15=Author.objects.filter(phone__startswith=155).values('name','age')
#
# 查找每个作者写的价格最高的书籍价格
res16=Book.objects.values('author').annotate(max=Max('price'))

# 查找每个作者的姓名以及出的书籍数量
res17=Book.objects.values('author__name').annotate(c=Count('title'))
#
# 查找书名是“跟金老板学开车”的书的出版社
res18=Publisher.objects.filter(book__title='跟金老板学开车')

# 查找书名是“跟金老板学开车”的书的出版社所在的城市
res19=Publisher.objects.filter(book__title='跟金老板学开车').values('city')

# 查找书名是“跟金老板学开车”的书的出版社的名称
res20=Publisher.objects.filter(book__title='跟金老板学开车').values('name')

# 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
res21=Publisher.objects.filter(book__title='跟金老板学开车').get().book_set.all().exclude(title='跟金老板学开车').values('title','price')
#
# 查找书名是“跟金老板学开车”的书的所有作者
res22=Author.objects.filter(books__title='跟金老板学开车')

# 查找书名是“跟金老板学开车”的书的作者的年龄
res23=Author.objects.filter(books__title='跟金老板学开车').values('age')

# 查找书名是“跟金老板学开车”的书的作者的手机号码


# 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
res25=Publisher.objects.filter(book__title='跟金老板学开车').values('book__title','book__price','book__author__name')

res26=Publisher.objects.filter(**{'book__title':'跟金老板学开车'})