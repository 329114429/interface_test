from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('', views.index, name='index'),
    re_path('<int:question_id>', views.detail, name='detail'),
    re_path('<int:question_id>/results/', views.results, name='results'),
    re_path('<int:question_id>/vote/', views.vote, name='vote'),
]
