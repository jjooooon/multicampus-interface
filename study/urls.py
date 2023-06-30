from django.urls import path,include

from . import views

app_name = 'study'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.problem_list, name='problem_list'),
    path('<int:problem_id>/', views.detail, name='detail'),
]