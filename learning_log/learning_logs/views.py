from django.shortcuts import render,HttpResponse


# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


