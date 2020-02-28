from django.db import models


# Create your models here.

# 当需要修改数据时,需要调用 makemigrations, 让Django迁移项目;

class Topic(models.Model):
    """用户学习主题, 数据库"""
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)  # 记录日期和时间

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text


class Entry(models.Model):
    '''需到的某个主题的具体知识, 数据库'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text[:50] + "..."

