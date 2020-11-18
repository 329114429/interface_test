from django.urls import path, re_path

from . import views

app_name = "polls"

urlpatterns = [
    re_path('', views.IndexView.as_view(), name='index'),
    re_path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    re_path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
    re_path('<int:question_id>/vote', views.vote, name='vote'),
]
