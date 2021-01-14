from django.urls import re_path

from vote import views, form

urlpatterns = [
    re_path('', views.SubjectView.as_view(), name='subjects'),
    re_path('api/teachers/', views.show_teachers, name='teachers'),
    re_path('praise/', views.praise_or_criticize),
    re_path('criticize/', views.praise_or_criticize),
    re_path('login/', views.login, name='login'),
    re_path('register/', views.register, name='register'),
    re_path('excel/', views.export_teachers_excel, name='excel'),
    re_path('teachers_data/', views.get_teachers_data, name='teachers_data'),
    re_path('/api/subjects/', views.SubjectView.as_view()),

]
