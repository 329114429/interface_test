from django.urls import re_path

from .views import show_index

urlpatterns = [
    re_path('', show_index, name='index'),
]
