from django.shortcuts import render, HttpResponse, reverse
from .models import Topic
from django.http import HttpResponseRedirect, Http404
from .forms import TopicFrom, EntryForm, Entry
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    """学习笔记主页"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_add')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个页面主题"""
    topic = Topic.objects.get(id=topic_id)  # 这个id是给topics.html

    # 请求确认主题数据当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_add')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """显示新添加的主题"""
    if request.method != "POST":
        # 未提交数据,创建一个空表单
        form = TopicFrom()
    else:
        form = TopicFrom(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
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
            new_entry = form.save(commit=False)  # 先不保存到数据库;
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑已有的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[entry_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
