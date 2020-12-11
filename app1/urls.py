from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.main, name='main'),
    path('grade', views.student, name='grade'),
    path('form', views.authorization, name='form'),
    path('homework', views.homework, name='homework'),
    path('timetable', views.timetable, name='timetable'),
    path('progress_table', views.progress_table, name='progress_table'),
    path('quit', views.quit, name='quit')
]
