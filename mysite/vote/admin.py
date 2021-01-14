from django.contrib import admin
from django.contrib.admin import ModelAdmin

from vote.models import Subject, Teacher


# Register your models here.

class SubjectModelAdmin(ModelAdmin):
    """学科模型管理"""
    list_display = ('no', 'name', 'intro', 'is_hot')
    ordering = ('no',)
    search_fields = ('name',)


class TeacherModelAdmin(ModelAdmin):
    """老师模型管理"""
    list_display = ('no', 'name', 'gender', 'birth', 'good_count', 'bad_count', 'subject')
    ordering = ('no',)
    search_fields = ('name',)


admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Teacher, TeacherModelAdmin)
