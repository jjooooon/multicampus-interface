from django.urls import path,include

from . import views

app_name = 'bigday'
urlpatterns = [
    path('', views.index, name='index'),
]