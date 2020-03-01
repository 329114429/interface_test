# user应用 的 url

from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = "users"  # 要注册

urlpatterns = [
    # 登录页面
    path("login/", LoginView.as_view(template_name='users/login.html'), name='login'),
]
