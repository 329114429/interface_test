from django.shortcuts import render, HttpResponse, reverse
from .models import Topic
from django.http import HttpResponseRedirect
from .forms import TopicFrom, EntryForm


# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """显示单个页面主题"""
    topic = Topic.objects.get(id=topic_id)  # 这个id是给topics.html
    entries = topic.entry_set.order_by('-date_add')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """显示新添加的主题"""
    if request.method != "POST":
        # 未提交数据,创建一个空表单
        form = TopicFrom()
    else:
        form = TopicFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """添加新的条目, 在特定的主题下,添加新条目"""
    topic = Topic.objects.get(id=topic_id)  # id 是一个与主题匹配的数字, 存在 topic_id 里

    if request.method != "POST":
        # 未提交数据,创建一个空
        form = EntryForm()
    else:
        # POST 提交数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # 先不保存到数据库;
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
