# Generated by Django 3.0.8 on 2020-11-29 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0002_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='mgr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrs.Emp', verbose_name='直接主管'),
        ),
    ]
