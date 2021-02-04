# user应用 的 url

from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls import url

app_name = "users"  # 要注册

urlpatterns = [
    # 登录页面
    path("login/", LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销页面
    path("logout/", views.logout_view, name='logout'),

    # 注册页面
    path("register", views.register, name='register'),
]
