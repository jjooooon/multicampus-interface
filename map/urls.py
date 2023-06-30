from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.map_create, name="create"),
    path('map_notebook/', views.map_notebook, name="map_notebook"),
    path('map_study/', views.map_study, name="map_study"),
]
