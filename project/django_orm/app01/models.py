from django.db import models

#出版社
class Publisher(models.Model):
  name = models.CharField(max_length=32)
  city = models.CharField(max_length=32)

  def __str__(self):
    return "<Publisher object: {} {}>".format(self.id, self.name)
#书籍
class Book(models.Model):
  title = models.CharField(max_length=32)
  publish_date = models.DateField(auto_now_add=True)
  price = models.DecimalField(max_digits=5,decimal_places=2)
  memo = models.TextField(null=True)
  #创建外键,关联Publisher
  Publisher = models.ForeignKey(to='Publisher',on_delete=models.CASCADE)

  def __str__(self):
    return "<Book object: {} {}>".format(self.id, self.title)

#作者
class Author(models.Model):
  name = models.CharField(max_length =32)
  age = models.IntegerField()
  phone = models.CharField(max_length=11)
  #创建多对多关联
  books = models.ManyToManyField(to='Book')

  def __str__(self):
    return "<Author object: {} {}>".format(self.id, self.name)