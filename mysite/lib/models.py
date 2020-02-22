from django.db import models

# Create your models here.

# 创建模型,book 四个字段 书名， 作者， 出版社， 出版日期
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

