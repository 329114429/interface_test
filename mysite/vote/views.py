import random
from io import BytesIO
import urllib.request
from tkinter import *
import json

import xlwt
import reportlab
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse, Http404
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection

from .models import Subject, Teacher
from .form import RegisterForm
from . import utils
from .models import User
from vote.utils import Captcha


# Create your views here.

class SubjectSerializers(serializers.ModelSerializer):
    # 编写序列化器
    class Meta:
        model = Subject
        fields = '__all__'


class SubjectsSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('no', 'name')


class TeacherSerializers(serializers.ModelSerializer):
    # 实现老师信息数据接口
    class Meta:
        model = Teacher
        exclude = ('subject',)


class CustomizedPagination(PageNumberPagination):
    # 指定分页器

    # 默认页大小
    page_size = 5

    # 页面大小对应的查询参数
    page_size_query_param = 'size'

    # 页面大小的最大值
    max_page_size = 50


def show_subjects(request):
    '''获取学科数据'''
    redis_cli = get_redis_connection()

    # 先尝试从缓存中获取学科数据
    data = redis_cli.get('vote:polls:subjects')

    if data:
        data = json.loads(data)  # 如果获取到学科数据就进行反序列化操作
    else:
        # 如果缓存中没有获取到学科数据就查询数据库
        queryset = Subject.objects.all()
        data = SubjectSerializers(queryset, many=True).data

        # 将查到的学科数据序列化后放到缓存中
        redis_cli.set('vote:polls:subjects', json.dumps(data), ex=86400)
    return Response({
        'code': 2000,
        'subjects': data,
    })


# @api_view(('GET',))
# def show_subjects(request: HttpRequest) -> HttpResponse:
#     """查看所有学科"""
#     subjects = Subject.objects.all().order_by('no')
#
#     # 创建序列化器对象并指定要序列化的模型
#     serializer = SubjectSerializers(subjects, many=True)
#
#     # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
#     return Response(serializer.data)

# queryset = Subject.objects.all()
# subjects = []
# for subject in queryset:
#     subjects.append({
#         'no': subject.no,
#         'name': subject.name,
#         'intro': subject.intro,
#         'isHot': subject.is_hot,
#     })
# return JsonResponse(subjects, safe=False)


class SubjectView(ListAPIView):
    # 通过queryset指定如何获取学科数据
    queryset = Subject.objects.all()
    # 通过serializer_class指定如何序列化学科数据
    serializer_class = SubjectSerializers

    # 指定如何分页
    pagination_class = CustomizedPagination


class TeacherView(ListAPIView):
    serializer_class = TeacherSerializers

    def get_queryset(self):
        queryset = Teacher.objects.defer('subject')
        try:
            sno = self.request.GET.get('sno', )
            queryset = queryset.filter(subject__no=sno)
            return queryset
        except ValueError:
            raise Http404


# @api_view(('GET',))
# def show_teachers(request: HttpRequest) -> HttpResponse:
#     """查看指定学科的老师"""
#     try:
#         sno = int(request.GET.get('sno'))
#         subject = Subject.objects.only('name').get(no=sno)
#         teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
#         subject_seri = SubjectsSimpleSerializers(subject)
#         teacher_seri = TeacherSerializers(teachers, many=True)
#         return Response({
#             'subject': subject_seri.data,
#             'teacher': teacher_seri.data,
#         })
#     except(TypeError, ValueError, Subject.DoesNotExist):
#         return Response(status=404)

# try:
#     sno = int(request.GET.get['sno'])
#     teachers = []
#     if sno:
#         subject = Subject.objects.only('name').get(no=sno)
#         teachers = Teacher.objects.filter(subject=subject).order_by('no')
#     return render(request, 'vote/teacher.html', {
#         'subject': subject,
#         'teachers': teachers,
#     })
# except (ValueError, Subject.DoesNotExist):
#     return redirect('/')


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    """好评"""
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('vote/praise'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {
                'code': 2000,
                'mesg': "操作成功",
                'count': count,
            }
        except (ValueError, Teacher.DoesNotExist):
            data = {
                'code': 2001,
                'mesg': "操作失败",
            }
    else:
        data = {
            'code': 2002,
            'mesg': "请先登录",
        }
    return JsonResponse(data)


def register(request):
    """注册"""
    page, hint = 'vote/templates/vote/register.html', ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            page = 'vote/login.html'
            hint = "注册成功,登录"
        else:
            hint = "请输入有效的注册信息"
    return render(request, page, {'hint': hint})


# def login(request):
#     if request.method == 'POST':
#         if request.session.test_cookie_worked():
#             request.session.delete_test_cookied()
#         else:
#             return HttpResponse("Please enable cookies and try again.")
#     request.session.set_test_cookie()
#     return render(request, 'vote/login.html')


def login(request: HttpRequest) -> HttpResponse:
    """登录"""
    hint = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = utils.gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = "用户名或密码错误"
        else:
            hint = "输入有效的用户名和密码"

    return render(request, 'vote/login.html', {'hint': hint})


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')


def get_captcha(request: HttpRequest) -> HttpResponse:
    """获取验证码视图函数"""
    captcha_text = utils.gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def export_teachers_excel(request):
    # 创建工作薄
    wb = xlwt.Workbook()

    # 添加工作表
    sheet = wb.add_sheet("老师信息表")

    # 查询老师所有信息
    queryset = Teacher.objects.all().select_related('subject')

    # 向excel表单中写表头
    colnames = ("姓名", "介绍", "好评数", "差评数", "学科")
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)

    # 向单元格写入老师信息
    props = ('name', 'detail', 'good_count', 'bad_count', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            value = getattr(teacher, prop, '')
            if isinstance(value, Subject):
                value = value.name
            sheet.write(row + 1, col, value)

    # 保存excel
    buffer = BytesIO()
    wb.save(buffer)

    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')

    # 中文文件名需处理百分号编码
    filename = urllib.request.quote('老师.xls')

    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment;filename*=utf-8''{filename}'
    return resp


def export_pdf(request: HttpRequest) -> HttpResponse:
    # 导出pdf
    buffer = BytesIO()
    pdf = Canvas(buffer)
    pdf.setFont("msyh", 80)
    pdf.setFillColorRGB(0.2, 0.5, 0.3)
    pdf.drawString(100, 550, 'hello world')
    pdf.showPage()
    pdf.save()
    resp = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    resp['content-disposition'] = 'inline;filename="demo.pdf"'
    return resp


def get_teachers_data(request):
    # 生成前端统计图表
    queryset = Teacher.objects.values('subject__name').annotate(good=('good_count'), bad=('bad_count'))
    names = [teacher.name for teacher in queryset]
    good_counts = [teacher.good_count for teacher in queryset]
    bad_counts = [teacher.bad_count for teacher in queryset]
    return JsonResponse({
        'names': names,
        'good_counts': good_counts,
        'bad_counts': bad_counts,
    })
