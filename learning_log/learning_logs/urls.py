# 定义learning_logs 的url模式


# 自己应用的urls

from django.urls import path, re_path
from . import views

app_name = "learning_logs"

urlpatterns = [
    # 主页
    path('index/', views.index, name='index'),  # 会跟主的url进行拼接, 所以这里直接是index

    # 显示所有主题
    path('topics/', views.topics, name='topics'),

    # 显示特定主题页面,单个页面
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),  # 这里要用re_path

    # path('topics/<int:topic_id>', views.topic, name='topic'),

    # 显示新添加主题, 单个主题
    path('new_topic/', views.new_topic, name='new_topic'),

    # 显示新添加的新条目页面
    re_path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name="new_entry"),

]
