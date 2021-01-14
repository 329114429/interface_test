# Generated by Django 3.0.8 on 2020-11-29 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('intro', models.CharField(max_length=512, verbose_name='简介')),
                ('is_hot', models.BooleanField(verbose_name='是否热门')),
            ],
            options={
                'verbose_name_plural': '学科',
                'db_table': 'tb_subject',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('gender', models.BooleanField(choices=[(True, '男'), (False, '女')], default=True, verbose_name='性别')),
                ('birth', models.DateField(null=True, verbose_name='出生日期')),
                ('intro', models.CharField(default='', max_length=512, verbose_name='')),
                ('good_count', models.IntegerField(default=0, verbose_name='好评数')),
                ('bad_count', models.IntegerField(default=0, verbose_name='差评数')),
                ('photo', models.CharField(max_length=255, verbose_name='照片')),
                ('subject',
                 models.ForeignKey(db_column='sno', on_delete=django.db.models.deletion.PROTECT, to='vote.Subject',
                                   verbose_name='学科')),
            ],
            options={
                'verbose_name_plural': '老师',
                'db_table': 'tb_teacher',
            },
        ),
    ]
