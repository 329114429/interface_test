from django.shortcuts import render, HttpResponse
from .models import Topic


# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)  # todo topics.html
