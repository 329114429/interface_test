from django.db import models


# Create your models here.


class Subject(models.Model):
    """学科"""
    no = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField(max_length=32, verbose_name="名称")
    intro = models.CharField(max_length=512, verbose_name="简介")
    is_hot = models.BooleanField(verbose_name="是否热门")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tb_subject'


class Teacher(models.Model):
    """老师"""
    no = models.AutoField(primary_key=True, verbose_name="编号")
    name = models.CharField(max_length=32, verbose_name="姓名")
    gender = models.BooleanField(default=True, choices=((True, "男"), (False, "女")), verbose_name="性别")
    birth = models.DateField(null=True, verbose_name="出生日期")
    intro = models.CharField(max_length=512, default="", verbose_name="")
    good_count = models.IntegerField(default=0, verbose_name="好评数")
    bad_count = models.IntegerField(default=0, verbose_name="差评数")
    photo = models.CharField(max_length=255, blank=True, verbose_name="照片")
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column="sno", verbose_name="学科")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tb_teacher'


class User(models.Model):
    """用户"""
    no = models.AutoField(primary_key=True, verbose_name="编号")
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=32, verbose_name="密码")
    tel = models.CharField(max_length=20, verbose_name="手机号", null=True)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="注册时间", null=True)
    last_visit = models.DateTimeField(null=True, verbose_name="最后登录时间")

    class Meta:
        db_table = 'tb_user'
        verbose_name = "用户"
        verbose_name_plural = "用户"
